import pygame
from database import *
from textbox import TextBox

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

	# -- NEEDS TO BE DONE ----------------------------------------------------------------------------------------- #
	# Make a def method here such as handle_event, to check if red_player_table.table[i][j] (& green) is full.. 	#
	# If full, pull from database with get_user_codename method in the database.py file								#
	# If not full you need to just leave the box blank, this will probably require a nested for						#
	# ------------------------------------------------------------------------------------------------------------- #	

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
		self.text_render = self.font.render(self.text, True, pygame.Color("White"))
		self.text_rect = self.text_render.get_rect(midtop=(self.rect.x + self.w/2, self.rect.y + 60))
		screen.blit(self.text_render, self.text_rect)
		pygame.draw.rect(screen, pygame.Color('White'), self.rect, 3)
