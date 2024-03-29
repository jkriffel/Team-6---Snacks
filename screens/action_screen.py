import pygame, sys, random
from functional_interfaces import Action_Table,Timer_Box,Action_Box,TextBox
from database import *
import socket
from udp.server import start_server
from pygame import mixer
import queue
import threading
import json
import time

def action_screen():
	pygame.init()

	SCREEN = pygame.display.set_mode((1280, 720))
	PLAYER_EVENT = pygame.USEREVENT + 1
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

	#create_client
	def create_client():

		serverIP     = "127.0.0.1"
		serverPort   = 7500

		localIP     = "127.0.0.1"
		localPort   = 7501

		# Create datagram socket
		UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

		message = "From Client To Server"
		UDPClientSocket.sendto(message.encode(), (serverIP, serverPort))

		UDPClientSocket.close()
		UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

		UDPClientSocket.bind((localIP, localPort))
		return UDPClientSocket

	#run_client
	def run_client(UDPClientSocket, q):
		
		bufferSize  = 1024
		localIP     = "127.0.0.1"
		localPort   = 7501

		print(f'UDP client up and listening on {localIP}:{localPort}')

		while True:
			message, _ = UDPClientSocket.recvfrom(bufferSize)
			message = message.decode()
			#print(f'client recieved message {message}')
			q.put(message)
			pygame.event.post(pygame.event.Event(PLAYER_EVENT))
		
		print("program complete")
	
	#get_font
	def get_font(size): # Returns Press-Start-2P in the desired size
		return pygame.font.Font("./assets/font.ttf", size)

	#set_music
	def set_music():
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

	def generate_message(player_names):
		messagesLR = [" zapped ", " lasered ", " blasted ", " sniped ", " tagged ", " vaporized "]
		action_message = player_names[0] + random.choice(messagesLR) + player_names[1]
		return action_message 

	#endregion

	#open the JSON file and read the corresponding dictionaries into to variables
	with open("table_data.json", "r") as file:
		team_data_from_json = json.load(file)

	#these dictionaries are formatted as 'ID': 'CODENAME'
	green_team_data = team_data_from_json[0]
	red_team_data = team_data_from_json[1]

	#red team score initialization
	for player_id in red_team_data.keys():
		red_team_data[player_id].append(0)
	#green team score initialization
	for player_id in green_team_data.keys():
		green_team_data[player_id].append(0)
	
	#clock for timer
	clock = pygame.time.Clock()

	set_music()
	pygame.display.set_caption("Action Screen")

	# create countdown text
	countdown_text_1 = get_font(25).render("Game Time", True, "PURPLE")
	countdown_text_1_rect = countdown_text_1.get_rect(topleft=(SCREEN_CENTER_X - 100, SCREEN_CENTER_Y - 310))

	# create player codename text 
	green_team_codename = get_font(25).render("Team 1", True, "GREEN")
	red_team_codename = get_font(25).render("Team 2", True, "RED")
	green_team_codename_rect = green_team_codename.get_rect(topleft=(SCREEN_CENTER_X - 565, SCREEN_CENTER_Y - 300))
	red_team_codename_rect = red_team_codename.get_rect(topleft=(SCREEN_CENTER_X + 585 - TABLE_WIDTH, SCREEN_CENTER_Y - 300))

	# create action box text
	action_box_text = get_font(25).render("Player Events", True, "PURPLE")
	action_box_text_rect = action_box_text.get_rect(topleft=(SCREEN_CENTER_X - 142, SCREEN_CENTER_Y + 275))

	# create team score text 
	green_team_score_text = get_font(25).render("SCORE", True, "GREEN")
	red_team_score_text = get_font(25).render("SCORE", True, "RED")
	green_team_score_text_rect = green_team_score_text.get_rect(topleft=(SCREEN_CENTER_X - 440, SCREEN_CENTER_Y + 255))
	red_team_score_text_rect = red_team_score_text.get_rect(topleft=(SCREEN_CENTER_X + 365, SCREEN_CENTER_Y + 255))

	# create tables for the player name and score 
	green_team_table   = Action_Table(SCREEN, SCREEN_CENTER_X - 565, SCREEN_CENTER_Y - 270, TABLE_WIDTH, TABLE_HEIGHT, green_team_data)
	red_team_table = Action_Table(SCREEN, SCREEN_CENTER_X + 235, SCREEN_CENTER_Y - 270, TABLE_WIDTH, TABLE_HEIGHT, red_team_data)

	# create box for countdown to go into
	countdown_timer_box = Timer_Box(SCREEN,SCREEN_CENTER_X - 32, SCREEN_CENTER_Y - 280, CLOCK_WIDTH, CLOCK_HEIGHT)

	# play the sound track
	mixer.music.play()

	# create box for action events to go into
	action_box = Action_Box(SCREEN,SCREEN_CENTER_X - 160, SCREEN_CENTER_Y - 280, ACTION_WIDTH, ACTION_HEIGHT, 'Game Started')

	# create box for total team score
	green_score_box = TextBox(SCREEN, SCREEN_CENTER_X - 298, SCREEN_CENTER_Y + 255, TEAM_BOX_WIDTH, TEAM_BOX_HEIGHT, 1)
	red_score_box = TextBox(SCREEN, SCREEN_CENTER_X + 502, SCREEN_CENTER_Y + 255, TEAM_BOX_WIDTH, TEAM_BOX_HEIGHT, 1)
	green_score_box.text = '0'
	red_score_box.text = '0'

	#creating queue. this allows client_thread to share live data with the main thread
	message_queue = queue.Queue()

	#start the server thread
	server_thread = threading.Thread(target=start_server)
	server_thread.daemon = True
	server_thread.start()

	print("server started")

	#creating the client UDPSocket, and thread
	UDPClient = create_client()
	client_thread = threading.Thread(target=run_client, args=(UDPClient, message_queue))
	client_thread.daemon = True
	client_thread.start()

	while True:
		SCREEN.fill("black")

		SCREEN.blit(countdown_text_1,countdown_text_1_rect)

		SCREEN.blit(green_team_codename, green_team_codename_rect)
		SCREEN.blit(red_team_codename, red_team_codename_rect)

		SCREEN.blit(action_box_text,action_box_text_rect)

		SCREEN.blit(green_team_score_text,green_team_score_text_rect)
		SCREEN.blit(red_team_score_text,red_team_score_text_rect)

		red_team_table.draw(SCREEN)
		green_team_table.draw(SCREEN)

		countdown_timer_box.draw(SCREEN)

		action_box.draw(SCREEN)

		green_score_box.draw(SCREEN)
		red_score_box.draw(SCREEN)

		pygame.display.flip()

		countdown_timer_box.update(clock.tick())

		if countdown_timer_box.game_over == True:
			countdown_text_1 = get_font(26).render("GAME OVER", True, "PURPLE")
			mixer.music.stop()

		mouse_pos = pygame.mouse.get_pos()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == PLAYER_EVENT:
				while not message_queue.empty():
					message = message_queue.get()
					#print(f'{message}: recieved from queue')
					#splices out player names from message string
					player_IDs = message.split(":")

					if player_IDs[0] in red_team_data:
						#generate message for action box
						red_player_name = red_team_data[player_IDs[0]][0]
						green_player_name = green_team_data[player_IDs[1]][0]
						action_box.add_message(generate_message([red_player_name, green_player_name]))

						#update the scores
						red_team_data[player_IDs[0]][1] += 10 
						red_team_table.player_data = red_team_data
						red_team_table.update()
						red_score_box.text = str(10+int(red_score_box.text))

					if player_IDs[0] in green_team_data:
						#generate message for action box
						green_player_name = green_team_data[player_IDs[0]][0]
						red_player_name = red_team_data[player_IDs[1]][0]
						action_box.add_message(generate_message([green_player_name, red_player_name]))
						
						#update the scores
						green_team_data[player_IDs[0]][1] += 10 
						green_team_table.player_data = green_team_data
						green_team_table.update()
						green_score_box.text = str(10+int(green_score_box.text))

					# Flashing High Team Score 
					if int(green_score_box.text) > int(red_score_box.text):
						green_score_box.flash = True
						red_score_box.flash = False
					elif int(red_score_box.text) > int(green_score_box.text):
						red_score_box.flash = True
						green_score_box.flash = False
					if int(green_score_box.text) == int(red_score_box.text):
						red_score_box.flash = False
						green_score_box.flash = False					
					
		pygame.display.update()