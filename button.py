import pygame

TEXT_COLOR = pygame.Color('Green')
BORDER_COLOR = pygame.Color('White')
FONT = pygame.font.Font("./assets/font.ttf", 10)

class Button:
    
    def __init__(self, x, y, w, h, text, text_color = TEXT_COLOR, border_color = BORDER_COLOR, font = FONT, action = lambda: print("button action not set")):
        self.rect = pygame.Rect(x, y, w, h)
        self.border_color = border_color
        self.font = font
        self.text_color = text_color

        #split text at lines b/c pygame doesn't deal with newline
        self.text_draw = []
        lines = text.split("\n")
        for i in range(len(lines)):
            self.text_draw.append(self.font.render(lines[i], True, self.text_color))

        self.action = action
    
    def draw(self, screen):
        for i in range(len(self.text_draw)):
            screen.blit(self.text_draw[i], (self.rect.x+5, self.rect.y+5+(2+FONT.get_height())*i))
        pygame.draw.rect(screen, self.border_color, self.rect, 3)
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.action()