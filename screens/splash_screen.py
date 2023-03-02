import pygame, sys

def splash_screen():

	def get_font(size): # Returns Press-Start-2P in the desired size
		return pygame.font.Font("./assets/font.ttf", size)
	

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
				pygame.display.quit()
				return
		
			if event.type == timer_event:
				pygame.display.quit()
				return

		pygame.display.update()