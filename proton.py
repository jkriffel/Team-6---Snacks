import pygame, sys

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Splash Screen")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("./assets/font.ttf", size)

#here is where the splash screen is executed
def splash_screen():
	pygame.display.set_caption("Splash Screen")
	splashImg = pygame.image.load("./assets/logo.jpg")
	splashImg = pygame.transform.scale(splashImg, (1280, 720))
	image_rect = splashImg.get_rect()

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
			if event.type == pygame.KEYUP:
				player_screen()
		pygame.display.update()

#here is where the player screen is executed
def player_screen():
	pygame.display.set_caption("Player Screen")

	SS_TEXT = get_font(35).render("PRESS ESC TO RETURN TO MAIN MENU", True, "White")
	SS_TEXT_RECT = SS_TEXT.get_rect(center=(640, 50))

	while True:
		SCREEN.fill("black")
		SCREEN.blit(SS_TEXT, SS_TEXT_RECT)

		mouse_pos = pygame.mouse.get_pos()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_ESCAPE:
					splash_screen()
		pygame.display.update()

#execute splash screen initially 
splash_screen()