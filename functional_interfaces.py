import pygame
from database import *

pygame.init()

TEXT_COLOR = pygame.Color('Green')
COLOR_DISABLED_BUTTON = pygame.Color('White')
COLOR_ENABLED_BUTTON = pygame.Color('green')
FONT_BUTTON = pygame.font.Font("./assets/font.ttf", 10)

COLOR_DISABLED_BOX = pygame.Color('White')
COLOR_ENABLED_BOX = pygame.Color('Purple')
FONT_BOX = pygame.font.Font("./assets/font.ttf", 20)

class TextBox:

	def __init__(self, screen, x, y, w, h, box_id):
		self.rect = pygame.Rect(x, y, w, h)
		self.color = COLOR_DISABLED_BOX
		self.text = ''
		self.text_draw = FONT_BOX.render('', True, self.color)
		self.active = False
		self.screen = screen
		self.box_id = box_id
		#box_ID = 0 is the small left box while 1 is the larger right box
		if box_id == 0:
			self.text_limit = 3
		else:
			self.text_limit = 10

	def draw(self, screen):
		self.color = COLOR_ENABLED_BOX if self.active else COLOR_DISABLED_BOX
		self.text_draw = FONT_BOX.render(self.text, True, self.color)
		screen.blit(self.text_draw, (self.rect.x+5, self.rect.y+5))
		pygame.draw.rect(screen, self.color, self.rect, 3)


class Player_Table:

	def __init__(self, screen, x, y, w, h):
		self.table = []
		#create a 2x15 table
		for i in range (15):
			left_box = TextBox(screen,  x,           y + (h/15 * i), w/4,           h/15, 0)
			right_box = TextBox(screen, x + w/4 + 5, y + (h/15 * i), (3 * w/4 - 5), h/15, 1)
			self.table.append([ left_box, right_box])
		self.screen = screen

	#Iterates through all rectangle entities in table and draws
	def draw(self, screen):
		for i in range(len(self.table)):
			for j in range(len(self.table[i])):
				self.table[i][j].draw(screen)

	def info_to_json(self):
		result = {}
		for i in range(len(self.table)):
			result[self.table[i][0].text] = self.table[i][1].text
		return result


	#Handles input events
	def handle_event(self, event):
		for i in range(len(self.table)):
			for j in range(len(self.table[i])):
				if event.type == pygame.MOUSEBUTTONDOWN:

					# check for input box click
					if self.table[i][j].rect.collidepoint(event.pos):
						self.table[i][j].active = not self.table[i][j].active
					else:
						self.table[i][j].active = False

				# when a text[i][j] box is active[i][j], process key inputs
				if event.type == pygame.KEYDOWN and self.table[i][j].active:

					#If enter key pressed access the database and exit textbox
					if event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE:
						
						#process events after user enters a ID
						if self.table[i][0].text != '' and self.table[i][0].active:
							self.table[i][1].text = get_user_codename(self.table[i][0].text) 

						#process events after user enters a codename
						if self.table[i][0].text != '' and self.table[i][1].active:
							create_user(self.table[i][0].text, self.table[i][1].text)
						
						self.table[i][j].active = not self.table[i][j].active
					
					#Handle text input
					elif event.key == pygame.K_BACKSPACE:
						self.table[i][j].text = self.table[i][j].text[:-1]
					
					elif len(self.table[i][j].text) < self.table[i][j].text_limit:
						if self.table[i][j].box_id == 1: 
							self.table[i][j].text += event.unicode
						elif self.table[i][j].box_id == 0 and event.unicode.isnumeric():
							self.table[i][j].text += event.unicode
				# re draw the texbox
				self.table[i][j].draw(self.screen)


class Action_Table:	

	def __init__(self, screen, x, y, w, h, player_data):
		self.table = []
		self.player_data = player_data.keys()
		self.screen = screen
		#create a 2x15 table
		for i in range (15):
			left_box =  TextBox(screen, x,                 y + (h/15 * i), 3 * w/4 - 5, h/15, 0)
			right_box = TextBox(screen, x + (3 * w/4 + 5), y + (h/15 * i), w/4        , h/15, 1)
			self.table.append([ left_box, right_box])
		
		#insert player data into the table
		for i in range(len(self.player_data)):
			if list(self.player_data)[i] != '':
				self.table[i][0].text = list(self.player_data)[i]
				self.table[i][1].text = '0' 

	#Iterates through all rectangle entities in table and draws
	def draw(self, screen):
		for i in range(len(self.table)):
			for j in range(len(self.table[i])):
				self.table[i][j].draw(screen)

	#Handles input events
	def handle_event(self, event):
		for i in range(len(self.table)):
			for j in range(len(self.table[i])):
				pass

class Timer_Box:

	def __init__(self, screen, x, y, w, h):
		self.table = []
		self.box = TextBox(screen, x, y, w, h, 0)
		self.screen = screen
		self.time_remaining = 360000
		self.game_over = False

	def draw(self, screen):
		rounded_time = self.time_remaining+999
		str_minutes = str(rounded_time//60000)
		str_seconds = str((rounded_time%60000)//1000)
		format_seconds = "0"+str_seconds if len(str_seconds)==1 else str_seconds
		self.box.text = str_minutes+":"+format_seconds
		self.box.draw(screen)
	
	def update(self, millis):
		self.time_remaining = self.time_remaining - millis
		if(self.time_remaining<=0):
			self.time_remaining = 0
			self.game_over = True

class Action_Box:
	def __init__(self, screen, x, y, w, h, text):
		self.table = []
		self.w = w
		self.h = h
		self.rect = pygame.Rect(x, y, w, h)
		self.screen = screen
		self.font = pygame.font.Font("./assets/font.ttf", 10)
		self.text = text

	#Iterates through all rectangle entities in table and draws
	def draw(self, screen):
		lines = self.text.split("\n")
		for i in range(len(lines)):
			self.text_render = self.font.render(lines[i], True, pygame.Color("White"))
			self.text_rect = self.text_render.get_rect(midtop=(self.rect.x + self.w/2, self.rect.y + 60 + 15*i))
			screen.blit(self.text_render, self.text_rect)
		pygame.draw.rect(screen, pygame.Color('White'), self.rect, 3)

class Button:

	def __init__(self, x, y, w, h, text, button_id):
			self.rect = pygame.Rect(x, y, w, h)
			self.border_color = COLOR_DISABLED_BUTTON
			self.font = FONT_BUTTON
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
					screen.blit(self.text_draw[i], (self.rect.x+5, self.rect.y+5+(2+FONT_BUTTON.get_height())*i))
			pygame.draw.rect(screen, self.border_color, self.rect, 3)

	def handle_event(self, event):
			self.border_color = COLOR_ENABLED_BUTTON if self.active else COLOR_DISABLED_BUTTON
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