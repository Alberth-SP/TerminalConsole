
from rect import *
import pygame 
class Letra:

	def __init__(self, x, y, letra, color=(255,255,255), size=40):
		self.x = x
		self.y = y
		self.letra = letra
		self.color = color
		self.tam = size
		my_font = pygame.font.Font(None, size)
		self.text = my_font.render(self.letra, True, color)

	def getText(self):
		return self.text


	def setColor(self, color):
		self.color = color

	def updateText(self):
		my_font = pygame.font.Font(None, self.tam)
		self.text = my_font.render(self.letra, True, self.color)

	def getPos(self):
		return (self.x, self.y)

	def show(self):
		rec = self.text.get_rect()
		return "{0} - ({1}-{2})".format(self.letra, self.x , self.y)

	def getPosFinal(self):
		rec = self.text.get_rect()
		return (self.x+ rec.width , self.y)
		


