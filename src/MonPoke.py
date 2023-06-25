from Constants import *
from random import randint, choice
import pygame

class CapturedMonPoke:
	def __init__(self, type_, health=100):
		self.type_ = type_
		self.health = health

	def big_attack(self):
		self.health -= randint(5, 7)
		hit  = randint(7, 10)
		return hit

	def small_attack(self):
		self.health -= randint(1, 3)
		hit = randint(3, 5)
		return hit
		
	def fight(self):
		option = ''
		while option not in ('BIG', 'SMALL'):
			option = input('Enter Attack Option: ').upper()
#options are
		#BIG, SMALL, HEAL, RUN
		
		if option == 'BIG':
			self.health -= randint(5, 7)
			hit  = randint(7, 10)
		elif option == 'SMALL':
			self.health -= randint(1, 3)
			hit = randint(3, 5)

		return hit

	def __str__(self):
		if self.type_ == MonPokeTypes.GIRAFFE:
			return '🦒'
		elif self.type_ == MonPokeTypes.SLIME_BALL:
			return '🟢'
		elif self.type_ == MonPokeTypes.HEDGEHOG:
			return '🦔'
		
	def blit_image(self, screen, x_coord, y_coord, no_background=False):
		path = 'monpoke/src/icons/'
		if no_background: path += 'alpha_monpokes/'
		else: path += 'monpokes/'

		if self.type_ == MonPokeTypes.GIRAFFE:
			path += 'Giraffe.png'
		elif self.type_ == MonPokeTypes.SLIME_BALL:
			path += 'Slime Ball.png'
		elif self.type_ == MonPokeTypes.HEDGEHOG:
			path += 'Hedgehog.png'

		img = pygame.image.load(path).convert_alpha()
		img = pygame.transform.scale(img, (50, 50))
		screen.blit(img, (x_coord*50, y_coord*50))

class MonPoke(CapturedMonPoke):

	def __init__(self, type_, x_pos, y_pos, health=100):
		super().__init__(type_, health)
		self.x_pos = x_pos
		self.y_pos = y_pos

	def fight(self):
		option = choice(['BIG', 'SMALL'])
		
		if option == 'BIG':
			self.health -= randint(5, 7)
			hit  = randint(7, 10)
		elif option == 'SMALL':
			self.health -= randint(1, 3)
			hit = randint(3, 5)

		return hit