import pygame, sys, random
from functional_interfaces import Action_Table,Timer_Box,Action_Box,TextBox
from database import *
from pygame import mixer
import json

def action_screen():
	pygame.init()

	SCREEN = pygame.display.set_mode((1280, 720))
	SCREEN_CENTER_X = 1280/2
	SCREEN_CENTER_Y = 720/2
	TABLE_WIDTH = 350
	TABLE_HEIGHT = 500
	CLOCK_WIDTH = 100
	CLOCK_HEIGHT = 50
	ACTION_WIDTH = 350
	ACTION_HEIGHT = 550
	TEAM_BOX_WIDTH = TABLE_WIDTH / 4
	TEAM_BOX_HEIGHT = TABLE_HEIGHT / 15

	#region functions
	def get_font(size): # Returns Press-Start-2P in the desired size
		return pygame.font.Font("./assets/font.ttf", size)

	def set_music():
		# sound
		mixer.init()

		tracks = {
		    1: "./assets/Track01.mp3",
		    2: "./assets/Track02.mp3",
		    3: "./assets/Track03.mp3",
		    4: "./assets/Track04.mp3",
		    5: "./assets/Track06.mp3",
		    6: "./assets/Track06.mp3",
		    7: "./assets/Track07.mp3",
		    8: "./assets/Track08.mp3",
		}

		# Picking a random track
		track_number = random.randint(1, 8)
		selected_track = tracks[track_number]

		mixer.music.load(selected_track)
		print(f"track{track_number}")

		mixer.music.set_volume(0.2)
	#endregion

	#open the JSON file and read the corresponding dictionaries into to variables
	with open("table_data.json", "r") as file:
		team_data = json.load(file)

	#these dictionaries are formatted as 'ID': 'CODENAME'
	green_team_data = team_data[0]
	red_team_data = team_data[1]

	#data tracked in dictionary by name this one becomes formatted as 'CODENAME': 'Score'
	red_team_scores = {}
	green_team_scores = {}

	#red team score initialization
	for player_data in red_team_data.values():
		red_team_scores[player_data] = 0
	#green team score initialization
	for player_data in green_team_data.values():
		green_team_scores[player_data] = 0
	
	#clock for timer
	clock = pygame.time.Clock()

	set_music()
	pygame.display.set_caption("Action Screen")

	# create countdown text
	countdown_text_1 = get_font(25).render("Game Time", True, "PURPLE")
	countdown_text_1_rect = countdown_text_1.get_rect(topleft=(SCREEN_CENTER_X - 100, SCREEN_CENTER_Y - 310))

	# create player codename text 
	team1_codename = get_font(25).render("Team 1", True, "GREEN")
	team2_codename = get_font(25).render("Team 2", True, "RED")
	team1_codename_rect = team1_codename.get_rect(topleft=(SCREEN_CENTER_X - 565, SCREEN_CENTER_Y - 300))
	team2_codename_rect = team2_codename.get_rect(topleft=(SCREEN_CENTER_X + 585 - TABLE_WIDTH, SCREEN_CENTER_Y - 300))

	# create action box text
	action_box_text = get_font(25).render("Player Events", True, "PURPLE")
	action_box_text_rect = action_box_text.get_rect(topleft=(SCREEN_CENTER_X - 142, SCREEN_CENTER_Y + 275))

	# create team score text 
	team1_score_text = get_font(25).render("SCORE", True, "GREEN")
	team2_score_text = get_font(25).render("SCORE", True, "RED")
	team1_score_text_rect = team1_score_text.get_rect(topleft=(SCREEN_CENTER_X - 440, SCREEN_CENTER_Y + 255))
	team2_score_text_rect = team2_score_text.get_rect(topleft=(SCREEN_CENTER_X + 365, SCREEN_CENTER_Y + 255))

	# create tables for the player name and score 
	green_team_table   = Action_Table(SCREEN, SCREEN_CENTER_X - 565, SCREEN_CENTER_Y - 270, TABLE_WIDTH, TABLE_HEIGHT, green_team_scores)
	red_team_table = Action_Table(SCREEN, SCREEN_CENTER_X + 235, SCREEN_CENTER_Y - 270, TABLE_WIDTH, TABLE_HEIGHT, red_team_scores)

	# create box for countdown to go into
	countdown_timer_box = Timer_Box(SCREEN,SCREEN_CENTER_X - 32, SCREEN_CENTER_Y - 280, CLOCK_WIDTH, CLOCK_HEIGHT)

	# play the sound track
	mixer.music.play()

	# create box for action events to go into
	action_box = Action_Box(SCREEN,SCREEN_CENTER_X - 160, SCREEN_CENTER_Y - 280, ACTION_WIDTH, ACTION_HEIGHT, 'Game Started')

	# create box for total team score
	team1_score_box = TextBox(SCREEN, SCREEN_CENTER_X - 298, SCREEN_CENTER_Y + 255, TEAM_BOX_WIDTH, TEAM_BOX_HEIGHT, 1)
	team2_score_box = TextBox(SCREEN, SCREEN_CENTER_X + 502, SCREEN_CENTER_Y + 255, TEAM_BOX_WIDTH, TEAM_BOX_HEIGHT, 1)
	team1_score_box.text = '0'
	team2_score_box.text = '0'


	while True:
		# Background Color
		SCREEN.fill("black")
		# Counterdown timer text
		SCREEN.blit(countdown_text_1,countdown_text_1_rect)
		# Player Codename Text
		SCREEN.blit(team1_codename, team1_codename_rect)
		SCREEN.blit(team2_codename, team2_codename_rect)
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

		if countdown_timer_box.game_over == True:
			countdown_text_1 = get_font(26).render("GAME OVER", True, "PURPLE")
			mixer.music.stop()

		#get message and update scores
		if not(countdown_timer_box.game_over) and random.random()<0.002:
			#this will simulate a message. it does not receive a message.
			message = "Wall Lasered Billy"
			action_box.text = action_box.text+"\n"+message
			#maybe put max lines functionality inside the action_box class?
			max_lines = 32
			if action_box.text.count("\n")>=max_lines:
				action_box.text = action_box.text[action_box.text.find("\n")+1:]
			players = message.split(" Lasered ")
			if players[0] in list(red_team_table.player_data):
				loc = list(red_team_table.player_data).index(players[0])
				red_team_table.table[loc][1].text = str(1+int(red_team_table.table[loc][1].text))
				team2_score_box.text = str(1+int(team2_score_box.text))
			elif players[0] in list(green_team_table.player_data):
				loc = list(green_team_table.player_data).index(players[0])
				green_team_table.table[loc][1].text = str(1+int(green_team_table.table[loc][1].text))
				team1_score_box.text = str(1+int(team1_score_box.text))


		mouse_pos = pygame.mouse.get_pos()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		
		pygame.display.update()