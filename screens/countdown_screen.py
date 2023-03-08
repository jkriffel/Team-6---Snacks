import pygame, sys
from PIL import Image 

def countdown_screen():

    def get_font(size): 
        return pygame.font.Font("./assets/font.ttf", size)
    
    pygame.init()
    SCREEN = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Countdown")

    # This is to start the counter at 30
    number = 30
    number_string = str(number)
    countdown_number = get_font(200).render(number_string, True, "White")
    countdown_number_RECT = countdown_number.get_rect(center = (640,340))

    # Text to say the game is starting 
    game_text = get_font(55).render("THE GAME WILL START IN", True, "white")
    game_text_rect = game_text.get_rect(center =(635, 60))

    # Intimidating text... 
    scary_text = get_font(55).render("TRUST NO ONE", True, "red")
    scary_text_rect = scary_text.get_rect(center = (635,550))

    # Timer for 30 seconds
    timer_event = pygame.USEREVENT + 1
    pygame.time.set_timer(timer_event, 320000)

    while number >= 0:
        SCREEN.fill("black")
        # Blits the first number "30" 
        SCREEN.blit(countdown_number, countdown_number_RECT)
        SCREEN.blit(game_text, game_text_rect)
        SCREEN.blit(scary_text, scary_text_rect)
        # This is where the number is decremented and made into a new variable to blit
        number = number - 1 
        number_string = str(number)
        countdown_number = get_font(200).render(number_string, True, "White")
        countdown_number_RECT = countdown_number.get_rect(center = (640,340))
        # Hold the cpu time for 1 second
        pygame.time.delay(1000)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # go to action screen after 30 seconds
            if event.type == timer_event:
                pygame.display.quit()
                return
        pygame.display.update()