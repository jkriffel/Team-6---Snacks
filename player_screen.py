import pygame, sys

SCREEN_CENTER_X = 1280/2
SCREEN_CENTER_Y = 720/2
CELL_WIDTH = 250
CELL_HEIGHT = 35

def player_screen():
	pygame.init()
	SCREEN = pygame.display.set_mode((1280, 720))
	pygame.display.set_caption("Player Screen")


	#temp_text = get_font(35).render("PRESS ESC TO RETURN TO MAIN MENU", True, "White")
	#temp_text_rect = temp_text.get_rect(center=(640, 50))

	#create team top texts
	team1_text = get_font(25).render("TEAM 1", True, "GREEN")
	team2_text = get_font(25).render("TEAM 2", True, "RED")
	team1_text_rect = team1_text.get_rect(topleft=(SCREEN_CENTER_X - 400, SCREEN_CENTER_Y - 310))
	team2_text_rect = team2_text.get_rect(topleft=(SCREEN_CENTER_X + 400 - CELL_WIDTH, SCREEN_CENTER_Y - 310))

	while True:
		
		#draw text and refresh screen
		SCREEN.fill("black")
		#SCREEN.blit(temp_text, temp_text_rect)
		SCREEN.blit(team1_text, team1_text_rect)
		SCREEN.blit(team2_text, team2_text_rect)
		pygame.display.update()

		mouse_pos = pygame.mouse.get_pos()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

	
def get_font(size): 
	return pygame.font.Font("./assets/font.ttf", size)