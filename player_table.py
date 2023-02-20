import pygame
from database import *

pygame.init()
COLOR_DISABLED = pygame.Color('White')
COLOR_ENABLED = pygame.Color('Purple')
FONT = pygame.font.Font("./assets/font.ttf", 20)

class Player_Table:

	def __init__(self, screen, x, y, w, h, text_limit):
		self.rect = []
		for i in range (15):
			#left_box = pygame.Rect(x, y + (h/15 * i), w/4, h/15)
			#right_box = pygame.Rect(x + w/4 + 5, y + (h/15 * i), (3 * w/4 - 5), h/15)
			self.rect.append([ pygame.Rect(x, y + (h/15 * i), w/4, h/15), pygame.Rect(x + w/4 + 5, y + (h/15 * i), (3 * w/4 - 5), h/15)])
			#del left_box
			#del right_box

		self.info = {}
		self.color = []
		for i in range (15):
			self.color.append([COLOR_DISABLED, COLOR_DISABLED]) 
		self.text = []
		for i in range (15):
			self.text.append(['', ''])
			
		self.text_draw = FONT.render('', True, COLOR_DISABLED)
		self.active = []
		for i in range (15):
			self.active.append([False, False]) 
		self.screen = screen
		self.text_limit = text_limit

	def draw(self, screen):
		for i in range(len(self.rect)):
			for j in range(len(self.rect[i])):
				self.text_draw = FONT.render(self.text[i][j], True, self.color[i][j])
				screen.blit(self.text_draw, (self.rect[i][j].x+5, self.rect[i][j].y+5))
				pygame.draw.rect(screen, self.color[i][j], self.rect[i][j], 3)

	def handle_event(self, event):
		for i in range(len(self.rect)):
			for j in range(len(self.rect[i])):
				self.color[i][j] = COLOR_ENABLED if self.active[i][j] else COLOR_DISABLED
				if event.type == pygame.MOUSEBUTTONDOWN:
					# check for input box click
					if self.rect[i][j].collidepoint(event.pos):
						self.active[i][j] = not self.active[i][j]
					else:
						self.active[i][j] = False
				# when a text[i][j] box is active[i][j], process key inputs
				if event.type == pygame.KEYDOWN and self.active[i][j]:

					#exit text[i][j] box
					if event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE:
						if self.text[i][0] != '' and self.active[i][0]:
							self.text[i][1] = get_user_codename(self.text[i][0]) 
						if self.text[i][0] != '' and self.active[i][1]:
							create_user(self.text[i][0], self.text[i][1])
							
						self.active[i][j] = not self.active[i][j]

					elif event.key == pygame.K_BACKSPACE:
						self.text[i][j] = self.text[i][j][:-1]
					elif len(self.text[i][j]) < self.text_limit:
						if not self.active[i][0]: 
							self.text[i][j] += event.unicode
						else:
							if event.unicode.isnumeric():
								self.text[i][j] += event.unicode
					# re draw the text[i][j].
				self.text_draw = FONT.render(self.text[i][j], True, self.color[i][j])
				pygame.display.flip()