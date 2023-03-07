import pygame
from database import *

pygame.init()
COLOR_DISABLED = pygame.Color('White')
COLOR_ENABLED = pygame.Color('Purple')
FONT = pygame.font.Font("./assets/font.ttf", 20)

class TextBox:

	def __init__(self, screen, x, y, w, h, box_id):
		self.rect = pygame.Rect(x, y, w, h)
		self.color = COLOR_DISABLED
		self.text = ''
		self.text_draw = FONT.render('', True, self.color)
		self.active = False
		self.screen = screen
		self.box_id = box_id
		#box_ID = 0 is the small left box while 1 is the larger right box
		if box_id == 0:
			self.text_limit = 3
		else:
			self.text_limit = 10

	def draw(self, screen):
		self.color = COLOR_ENABLED if self.active else COLOR_DISABLED
		self.text_draw = FONT.render(self.text, True, self.color)
		screen.blit(self.text_draw, (self.rect.x+5, self.rect.y+5))
		pygame.draw.rect(screen, self.color, self.rect, 3)