import pygame

TEXT_COLOR = pygame.Color('Green')
BORDER_COLOR_DISABLED = pygame.Color('White')
BORDER_COLOR_ENABLED = pygame.Color('green')
FONT = pygame.font.Font("./assets/font.ttf", 10)

class Button:
    
    def __init__(self, x, y, w, h, text, button_id):
        self.rect = pygame.Rect(x, y, w, h)
        self.border_color = BORDER_COLOR_DISABLED
        self.font = FONT
        self.text_color = TEXT_COLOR
        self.active = False
        self.button_id = button_id

        #split text at lines b/c pygame doesn't deal with newline
        #lines[0] is also used to determine function keyboard inputs
        self.text_draw = []
        self.lines = text.split("\n")
        for i in range(len(self.lines)):
            self.text_draw.append(self.font.render(self.lines[i], True, self.text_color))
    
    def draw(self, screen):
        for i in range(len(self.text_draw)):
            screen.blit(self.text_draw[i], (self.rect.x+5, self.rect.y+5+(2+FONT.get_height())*i))
        pygame.draw.rect(screen, self.border_color, self.rect, 3)
    
    def handle_event(self, event):
        self.border_color = BORDER_COLOR_ENABLED if self.active else BORDER_COLOR_DISABLED
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.key.key_code(self.lines[0]):
                self.active = True
            else:
                self.active = False