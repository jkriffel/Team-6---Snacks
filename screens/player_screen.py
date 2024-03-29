import pygame, sys
from functional_interfaces import Player_Table, Button
from database import *
import json

def player_screen():

	pygame.init()

	SCREEN = pygame.display.set_mode((1280, 720))
	SCREEN_CENTER_X = 1280/2
	SCREEN_CENTER_Y = 720/2
	TABLE_WIDTH = 350
	TABLE_HEIGHT = 500

	def get_font(size): # Returns Press-Start-2P in the desired size
		return pygame.font.Font("./assets/font.ttf", size)

	def create_buttons(x, y, w, h):
		return [
			Button(x,      	  y, w/12, h, "F1\nEdit\nGame",       1),
			Button(x+w/12, 	  y, w/12, h, "F2\nGame\nParameters", 2),
			Button(x+2*w/12,  y, w/12, h, "F3", 									3),
			Button(x+4*w/12,  y, w/12, h, "F5\nStart\nGame", 			5),
			Button(x+6*w/12,  y, w/12, h, "F7\n", 								7),
			Button(x+7*w/12,  y, w/12, h, "F8\nView\nGame", 			8),
			Button(x+9*w/12,  y, w/12, h, "F10\nFlick\nSync", 		10),
			Button(x+11*w/12, y, w/12, h, "F12\nClear\nGame", 		12),
		]
		

	pygame.display.set_caption("Player Screen")

	# create player id top text
	team1_id_text = get_font(25).render("ID", True, "GREEN")
	team2_id_text = get_font(25).render("ID", True, "RED")
	team1_id_text_rect = team1_id_text.get_rect(topleft=(SCREEN_CENTER_X - 500, SCREEN_CENTER_Y - 300))
	team2_id_text_rect = team2_id_text.get_rect(topleft=(SCREEN_CENTER_X + 450 - TABLE_WIDTH, SCREEN_CENTER_Y - 300))

	# create player codename text
	team1_codename_text = get_font(25).render("CODENAME", True, "GREEN")
	team2_codename_text = get_font(25).render("CODENAME", True, "RED")
	team1_codename_text_rect = team1_codename_text.get_rect(topleft=(SCREEN_CENTER_X - 400, SCREEN_CENTER_Y - 300))
	team2_codename_text_rect = team2_codename_text.get_rect(topleft=(SCREEN_CENTER_X + 550 - TABLE_WIDTH, SCREEN_CENTER_Y - 300))

	# call table function to create player entries
	red_team_table = Player_Table(SCREEN, SCREEN_CENTER_X - 500, SCREEN_CENTER_Y - 265, TABLE_WIDTH, TABLE_HEIGHT)
	green_team_table = Player_Table(SCREEN, SCREEN_CENTER_X + 100, SCREEN_CENTER_Y - 265, TABLE_WIDTH, TABLE_HEIGHT)

	#create buttons
	buttons = create_buttons(0, 640, 1280, 80)
	button_actions = {
					1: "entering edit mode",
					2: "Game Parameters",
					3: "I am a useless button",
					5: "starting game lol",
					7: "I am also a useless button",
					8: "view game",
					10: "flick sync",
					12: "clear game",
				}
	
	#game loop
	while True:
		
		SCREEN.fill("black")

		SCREEN.blit(team1_id_text, team1_id_text_rect)
		SCREEN.blit(team2_id_text, team2_id_text_rect)

		SCREEN.blit(team1_codename_text, team1_codename_text_rect)
		SCREEN.blit(team2_codename_text, team2_codename_text_rect)

		red_team_table.draw(SCREEN)
		green_team_table.draw(SCREEN)

		for button in buttons:
			button.draw(SCREEN)
						
		
		pygame.display.flip()
		
		mouse_pos = pygame.mouse.get_pos()

		for event in pygame.event.get():

			red_team_table.handle_event(event)
			green_team_table.handle_event(event)

			#handle button presses
			for button in buttons:
				button.handle_event(event)
				if button.active:

					if button.button_id in button_actions:
							print(button_actions[button.button_id])

							if button.button_id == 5:
								table_data = [red_team_table.info_to_json(), green_team_table.info_to_json()]
								with open("table_data.json", "w") as json_file:
									json.dump(table_data, json_file, indent=4)
								pygame.display.quit()
								return

							elif button.button_id == 12:
								for i in range(len(red_team_table.table)):
									for j in range(len(red_team_table.table[i])):
										red_team_table.table[i][j].text = ""
								for i in range(len(green_team_table.table)):
									for j in range(len(green_team_table.table[i])):
										green_team_table.table[i][j].text = ""

							else:
									print(f"No real action for button {button.button_id}")
					button.active = not button.active


			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		pygame.display.update()
