from rect import *
import pygame

class Consola(Rect, pygame.sprite.Sprite):

	def __init__(self, x, y, width, height, line=1, borde=1):
		super().__init__(x, y, width, height)
		self.color = (255,255,255)
		self.borde = borde
		self.line = line

	def setColor(self, color):
		self.color = color


	def draw(self, screen):
		pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height),self.line, self.borde)
