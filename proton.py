import pygame, sys
from textbox import TextBox
from button import Button
from player_table import Player_Table
from database import *

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
SCREEN_CENTER_X = 1280/2
SCREEN_CENTER_Y = 720/2
TABLE_WIDTH = 350
TABLE_HEIGHT = 500
pygame.display.set_caption("Splash Screen")

def get_font(size): # Returns Press-Start-2P in the desired size
	return pygame.font.Font("./assets/font.ttf", size)

def create_buttons(x, y, w, h):
	return [
		Button(x, y, w/12, h, "F1\nEdit\nGame", action = lambda:print("F1 Edit Game")),
		Button(x+w/12, y, w/12, h, "F2\nGame\nParameters", action = lambda:print("F2 Game Parameters")),
		Button(x+2*w/12, y, w/12, h, "F3\nStart\nGame", action = lambda:print("F3 Start Game")),
		Button(x+4*w/12, y, w/12, h, "F5\nPreEntered\nGame", action = lambda:print("F5 PreEntered Game")),
		Button(x+6*w/12, y, w/12, h, "F7\n", action = lambda:print("F7")),
		Button(x+7*w/12, y, w/12, h, "F8\nView\nGame", action = lambda:print("F8 View Game")),
		Button(x+9*w/12, y, w/12, h, "F10\nFlick\nSync", action = lambda:print("F10 Flick Sync")),
		Button(x+11*w/12, y, w/12, h, "F12\nClear\nGame", action = lambda:print("F12 Clear Game")),
	]

#here is where the splash screen is executed
def splash_screen():
	pygame.display.set_caption("Splash Screen")
	splashImg = pygame.image.load("./assets/logo.jpg")
	splashImg = pygame.transform.scale(splashImg, (1280, 720))
	image_rect = splashImg.get_rect()

	#top text
	SS_TEXT = get_font(35).render("PRESS ANY KEY TO CONTINUE", True, "White")
	SS_TEXT_RECT = SS_TEXT.get_rect(center=(640, 50))

	#create the game loop
	while True:
		SCREEN.fill("black")
		SCREEN.blit(splashImg, image_rect)
		SCREEN.blit(SS_TEXT, SS_TEXT_RECT)
		pygame.display.flip()

		mouse_pos = pygame.mouse.get_pos()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			#go to player screen
			if event.type == pygame.KEYUP:
				player_screen()

		pygame.display.update()

#here is where the player screen is executed
def player_screen():
	pygame.display.set_caption("Player Screen")


	#temp_text = get_font(35).render("PRESS ESC TO RETURN TO MAIN MENU", True, "White")
	#temp_text_rect = temp_text.get_rect(center=(640, 50))

	#create team top texts
	team1_text = get_font(25).render("TEAM 1", True, "GREEN")
	team2_text = get_font(25).render("TEAM 2", True, "RED")
	team1_text_rect = team1_text.get_rect(topleft=(SCREEN_CENTER_X - 400, SCREEN_CENTER_Y - 310))
	team2_text_rect = team2_text.get_rect(topleft=(SCREEN_CENTER_X + 550 - TABLE_WIDTH, SCREEN_CENTER_Y - 310))

	#call table function to create player entries

	red_team_table = Player_Table(SCREEN, SCREEN_CENTER_X - 500, SCREEN_CENTER_Y - 285, TABLE_WIDTH, TABLE_HEIGHT)
	green_team_table = Player_Table(SCREEN, SCREEN_CENTER_X + 100, SCREEN_CENTER_Y - 285, TABLE_WIDTH, TABLE_HEIGHT)

	#create buttons
	buttons = create_buttons(0, 640, 1280, 80)
	
	#game loop
	while True:
		
		#draw text and refresh screen
		SCREEN.fill("black")
		#SCREEN.blit(temp_text, temp_text_rect)
		SCREEN.blit(team1_text, team1_text_rect)
		SCREEN.blit(team2_text, team2_text_rect)
		
		red_team_table.draw(SCREEN)
		green_team_table.draw(SCREEN)

		#draw buttons
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

			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			#return to splash screen
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_ESCAPE:
					splash_screen()

		pygame.display.update()

#execute splash screen initially 
splash_screen()