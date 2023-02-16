import pygame

pygame.init()
COLOR_DISABLED = pygame.Color('White')
COLOR_ENABLED = pygame.Color('Darkgrey')
FONT = pygame.font.Font("./assets/font.ttf", 25)

class TextBox:

	def __init__(self, screen, x, y, w, h):
		self.rect = pygame.Rect(x, y, w, h)
		self.color = COLOR_DISABLED
		self.text = ''
		self.text_draw = FONT.render('', True, self.color)
		self.active = False
		self.screen = screen

	def draw(self, screen):
		screen.blit(self.text_draw, (self.rect.x+5, self.rect.y+5))
		pygame.draw.rect(screen, self.color, self.rect, 3)

	def handle_event(self, event):
		self.color = COLOR_ENABLED if self.active else COLOR_DISABLED
		if event.type == pygame.MOUSEBUTTONDOWN:
			# check for input box click
			if self.rect.collidepoint(event.pos):
				self.active = not self.active
			else:
				self.active = False
		# when a text box is active, process key inputs
		if event.type == pygame.KEYDOWN and self.active:

			#exit text box
			if event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE:
				self.active = not self.active

			elif event.key == pygame.K_BACKSPACE:
				self.text = self.text[:-1]
			elif len(self.text) < 9:
				self.text += event.unicode
			# re draw the text.
			self.text_draw = FONT.render(self.text, True, self.color)