import pygame
from database import *
from textbox import TextBox

class Player_Table:

	def __init__(self, screen, x, y, w, h):
		self.table = []
		#create a 2x15 table
		for i in range (15):
			left_box = TextBox(screen, x, y + (h/15 * i), w/4, h/15, 0)
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

	def __init__(self, screen, x, y,LW,LH,RW,RH):
		self.table = []
		#create a 2x15 table
		for i in range (15):
			left_box = TextBox(screen,x,y +(LH/15 * i), LW, LH/15,0)
			right_box = TextBox(screen,x,y +(RH/15 * i), 3 * RW/4 - 5, RH/15,0)
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

class Timer_Box:

	def __init__(self, screen, x, y,w,h):
		self.table = []
		left_box = TextBox(screen,x,y +(h/15), w, h/15,0)
		#right_box = TextBox(screen,x,y +(h/15), 3 * w/4 - 5, h/15,0)
		right_box = TextBox(screen,x,y +(h/15), 0, 0,0)
		self.table.append([ left_box, right_box])
		self.screen = screen

	#Iterates through all rectangle entities in table and draws
	def draw(self, screen):
		for i in range(len(self.table)):
			for j in range(len(self.table[i])):
				self.table[i][j].draw(screen)

class Action_Box:
	def __init__(self, screen, x, y,w,h):
		self.table = []
		left_box = TextBox(screen,x,y +(h/15), w, h/15,0)
		#right_box = TextBox(screen,x,y +(h/15), 3 * w/4 - 5, h/15,0)
		right_box = TextBox(screen,x,y +(h/15), 0, 0,0)
		self.table.append([ left_box, right_box])
		self.screen = screen

	#Iterates through all rectangle entities in table and draws
	def draw(self, screen):
		for i in range(len(self.table)):
			for j in range(len(self.table[i])):
				self.table[i][j].draw(screen)

class Total_Box:
	def __init__(self, screen, x, y,w,h):
		self.table = []
		left_box = TextBox(screen,x,y +(h/15), w, h/15,0)
		#right_box = TextBox(screen,x,y +(h/15), 3 * w/4 - 5, h/15,0)
		right_box = TextBox(screen,x,y +(h/15), 0, 0,0)
		self.table.append([ left_box, right_box])
		self.screen = screen

	#Iterates through all rectangle entities in table and draws
	def draw(self, screen):
		for i in range(len(self.table)):
			for j in range(len(self.table[i])):
				self.table[i][j].draw(screen)