import pygame, sys

SCREEN_CENTER_X = 1280/2
SCREEN_CENTER_Y = 720/2
CELL_WIDTH = 250
CELL_HEIGHT = 35

def splash_screen():
	RUNNING = True
	pygame.init()
	SCREEN = pygame.display.set_mode((1280, 720))
	pygame.display.set_caption("Splash Screen")
	splashImg = pygame.image.load("./assets/logo.jpg")
	splashImg = pygame.transform.scale(splashImg, (1280, 720))
	image_rect = splashImg.get_rect()

	#top text
	SS_TEXT = get_font(35).render("PRESS ANY KEY TO CONTINUE", True, "White")
	SS_TEXT_RECT = SS_TEXT.get_rect(center=(640, 50))


	timer_event = pygame.USEREVENT + 1
	pygame.time.set_timer(timer_event, 3000)
	#create the game loop
	while RUNNING:
		SCREEN.fill("black")
		SCREEN.blit(splashImg, image_rect)
		SCREEN.blit(SS_TEXT, SS_TEXT_RECT)
		pygame.display.flip()
	
		mouse_pos = pygame.mouse.get_pos()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			if event.type == timer_event:
				RUNNING = False

		pygame.display.update()
	pygame.quit()

def get_font(size): 
	return pygame.font.Font("./assets/font.ttf", size)