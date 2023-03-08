import pygame, sys
from player_table import Action_Table,Timer_Box,Action_Box,Total_Box
from button import Button
from database import *

def action_screen(player_tables):
	pygame.init()

	SCREEN = pygame.display.set_mode((1280, 720))
	SCREEN_CENTER_X = 1280/2
	SCREEN_CENTER_Y = 720/2
	TABLE_WIDTH = 350
	TABLE_HEIGHT = 500
	LEFT_WIDTH = 450
	LEFT_HEIGHT = 500
	RIGHT_WIDTH = 450
	RIGHT_HEIGHT = 500
	CLOCK_WIDTH = 150
	CLOCK_HEIGHT = 1000
	ACTION_WIDTH = 300
	ACTION_HEIGHT = 4500
	TEAM_BOX_WIDTH = 150
	TEAM_BOX_HEIGHT = 800

	#data tracked in dictionary by name
	red_team_scores = {}
	green_team_scores = {}
	#red team score initialization
	for player_data in player_tables[0].table:
		red_team_scores[player_data[1].text] = 0
	#green team score initialization
	for player_data in player_tables[1].table:
		green_team_scores[player_data[1].text] = 0
	
	#clock for timer
	clock = pygame.time.Clock()

	# Font that Josh likes -_-
	def get_font(size): # Returns Press-Start-2P in the desired size
		return pygame.font.Font("./assets/font.ttf", size)


	pygame.display.set_caption("Action Screen")

	# create team top texts
	team1_text = get_font(25).render("TEAM 1", True, "GREEN")
	team2_text = get_font(25).render("TEAM 2", True, "RED")
	team1_text_rect = team1_text.get_rect(topleft=(SCREEN_CENTER_X - 475, SCREEN_CENTER_Y - 340))
	team2_text_rect = team2_text.get_rect(topleft=(SCREEN_CENTER_X + 675 - TABLE_WIDTH, SCREEN_CENTER_Y - 340))

	# create countdown text (the count down needs to be implemented - kirby)
	countdown_text_1 = get_font(25).render("THE GAME", True, "PURPLE")
	countdown_text_2 = get_font(25).render("ENDS IN", True, "PURPLE")
	countdown_text_1_rect = countdown_text_1.get_rect(topleft=(SCREEN_CENTER_X - 100, SCREEN_CENTER_Y - 340))
	countdown_text_2_rect = countdown_text_2.get_rect(topleft=(SCREEN_CENTER_X - 85, SCREEN_CENTER_Y - 300))


	# create player codename text 
	team1_codename = get_font(25).render("CODENAME", True, "GREEN")
	team2_codename = get_font(25).render("CODENAME", True, "RED")
	team1_codename_rect = team1_codename.get_rect(topleft=(SCREEN_CENTER_X - 565, SCREEN_CENTER_Y - 300))
	team2_codename_rect = team2_codename.get_rect(topleft=(SCREEN_CENTER_X + 585 - TABLE_WIDTH, SCREEN_CENTER_Y - 300))

	# create team score texts
	team1_score = get_font(25).render("SCORE", True, "GREEN")
	team2_score = get_font(25).render("SCORE", True, "RED")
	team1_score_rect = team1_text.get_rect(topleft=(SCREEN_CENTER_X - 300, SCREEN_CENTER_Y - 300))
	team2_score_rect = team2_text.get_rect(topleft=(SCREEN_CENTER_X + 850 - TABLE_WIDTH, SCREEN_CENTER_Y - 300))

	# create action box text
	action_box_text = get_font(25).render("PLAYER EVENTS", True, "BLUE")
	action_box_text_rect = action_box_text.get_rect(topleft=(SCREEN_CENTER_X - 160, SCREEN_CENTER_Y - 110))

	# create team score text 
	team1_score_text = get_font(25).render("TEAM 1 SCORE", True, "GREEN")
	team2_score_text = get_font(25).render("TEAM 2 SCORE", True, "RED")
	team1_score_text_rect = team1_score_text.get_rect(topleft=(SCREEN_CENTER_X - 625, SCREEN_CENTER_Y + 260))
	team2_score_text_rect = team2_score_text.get_rect(topleft=(SCREEN_CENTER_X + 175, SCREEN_CENTER_Y + 260))

	# create tables for the player name and score 
	red_team_table = Action_Table(SCREEN, SCREEN_CENTER_X - 625, SCREEN_CENTER_Y - 270, LEFT_WIDTH, LEFT_HEIGHT, RIGHT_WIDTH, RIGHT_HEIGHT)
	green_team_table = Action_Table(SCREEN, SCREEN_CENTER_X + 175, SCREEN_CENTER_Y - 270, LEFT_WIDTH, LEFT_HEIGHT, RIGHT_WIDTH, RIGHT_HEIGHT)

	# create box for countdown to go into
	countdown_timer_box = Timer_Box(SCREEN,SCREEN_CENTER_X - 75,SCREEN_CENTER_Y - 320, CLOCK_WIDTH, CLOCK_HEIGHT)

	# create box for action events to go into
	action_box = Action_Box(SCREEN,SCREEN_CENTER_X - 150, SCREEN_CENTER_Y - 370, ACTION_WIDTH, ACTION_HEIGHT)

	# create box for total team score
	team1_score_box = Total_Box(SCREEN, SCREEN_CENTER_X - 315, SCREEN_CENTER_Y + 190, TEAM_BOX_WIDTH, TEAM_BOX_HEIGHT)
	team2_score_box = Total_Box(SCREEN, SCREEN_CENTER_X + 485, SCREEN_CENTER_Y + 190, TEAM_BOX_WIDTH, TEAM_BOX_HEIGHT)


	while True:
		# Background Color
		SCREEN.fill("black")
		# Top Text 
		SCREEN.blit(team1_text, team1_text_rect)
		SCREEN.blit(team2_text, team2_text_rect)
		# Counterdown timer text
		SCREEN.blit(countdown_text_1,countdown_text_1_rect)
		SCREEN.blit(countdown_text_2,countdown_text_2_rect)
		# Player Codename Text
		SCREEN.blit(team1_codename, team1_codename_rect)
		SCREEN.blit(team2_codename, team2_codename_rect)
		# Top Score Text
		SCREEN.blit(team1_score, team1_score_rect)
		SCREEN.blit(team2_score, team2_score_rect)
		# Action box text
		SCREEN.blit(action_box_text,action_box_text_rect)
		# Team score text 
		SCREEN.blit(team1_score_text,team1_score_text_rect)
		SCREEN.blit(team2_score_text,team2_score_text_rect)
		# Player name & Player Score box 
		red_team_table.draw(SCREEN)
		green_team_table.draw(SCREEN)
		# Clock box 
		countdown_timer_box.draw(SCREEN)
		# Action box
		action_box.draw(SCREEN)
		# Total team score boxes
		team1_score_box.draw(SCREEN)
		team2_score_box.draw(SCREEN)

		pygame.display.flip()

		#update timer
		countdown_timer_box.update(clock.tick())

		mouse_pos = pygame.mouse.get_pos()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		
		pygame.display.update()