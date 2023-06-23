from Constants import *
import pygame

class PickUp:

	def __init__(self, type_):
		self.type_ = type_

	def __str__(self):
		if self.type_ == PickUpTypes.APPLE:
			return '🍎'
		elif self.type_ == PickUpTypes.BAGUETTE:
			return '🥖'
		elif self.type_ == PickUpTypes.CAKE:
			return '🎂'
		elif self.type_ == PickUpTypes.CHICKEN:
			return '🍗'
		elif self.type_ == PickUpTypes.CABBAGE:
			return '🪻'

	def blit_image(self, screen, x_coord, y_coord, no_background=False):
		path = 'monpoke/src/icons/'
		if no_background: path += 'alpha_pickups/'
		else: path += 'pickups/'
			
		if self.type_ == PickUpTypes.APPLE:
			path += 'Apple.png'
		elif self.type_ == PickUpTypes.BAGUETTE:
			path += 'Baguette.png'
		elif self.type_ == PickUpTypes.CAKE:
			path += 'Cake.png'
		elif self.type_ == PickUpTypes.CHICKEN:
			path += 'Chicken.png'
		elif self.type_ == PickUpTypes.CABBAGE:
			path += 'Cabbage.png'
		
		img = pygame.image.load(path).convert_alpha()
		img = pygame.transform.scale(img, (50, 50))
		
		screen.blit(img, (x_coord*50, y_coord*50))

	def use_pickup(self):
		if self.type_ == PickUpTypes.APPLE:
			return 10
		elif self.type_ == PickUpTypes.BAGUETTE:
			return 20
		elif self.type_ == PickUpTypes.CAKE:
			return 30
		elif self.type_ == PickUpTypes.CHICKEN:
			return 40
		elif self.type_ == PickUpTypes.CABBAGE:
			return 50