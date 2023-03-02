import pygame, sys

def action_screen():
	pygame.init()

	SCREEN = pygame.display.set_mode((1280, 720))
	SCREEN_CENTER_X = 1280/2
	SCREEN_CENTER_Y = 720/2
	TABLE_WIDTH = 350
	TABLE_HEIGHT = 500

	pygame.display.set_caption("Action Screen")

	while True:
		SCREEN.fill("black")
		pygame.display.flip()

		mouse_pos = pygame.mouse.get_pos()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		
		pygame.display.update()