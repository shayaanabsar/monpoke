from Constants import *
from MonPoke import *
from random import choices
from PickUp import *
import pygame

def generate_map_component():
	return choices(list(MapItems), weights=(90, 2, 3, 1, 1), k=1)[0]


def generate_monpoke_type():
	return choices(list(MonPokeTypes),
	               weights=(13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1),
	               k=1)[0]

def generate_pickup_type():
	return choices(list(PickUpTypes),
	               weights=(5, 4, 3, 2, 1),
	               k=1)[0]
class Map:

	def __init__(self):
		self.map_components = {(0, 0): MapItems.GRASS}
		self.monpokes = {}
		self.pickups = {}

	def get_component(self, j, i):
		if (j, i) not in self.map_components:
			self.map_components[(j, i)] = generate_map_component()

			if self.map_components[(j, i)] == MapItems.MONPOKE:
				type_ = generate_monpoke_type()
				monpoke = MonPoke(type_, j, i)
				self.monpokes[(j, i)] = monpoke

			if self.map_components[(j, i)]  == MapItems.PICKUP:
				type_ = generate_pickup_type()
				pickup = PickUp(type_)
				self.pickups[(j, i)] = pickup
		return self.map_components[(j, i)]
		

	def draw_map(self, player):
		for j in range(player.y_pos - 5, player.y_pos + 5):
			for i in range(player.x_pos - 5, player.x_pos + 5):
				if (player.y_pos, player.x_pos) == (j, i):
					print('🧕', end='')
				else:
					component = self.get_component(j, i)
					
					if component == MapItems.GRASS: print('🟩', end='')
					elif component == MapItems.HOUSE: print('🏠', end='')
					elif component == MapItems.TREE: print('🌳', end='')
					elif component == MapItems.MONPOKE: print(self.monpokes[(j, i)], end='')
					elif component == MapItems.PICKUP: print(self.pickups[(j, i)], end='')

			print('')

	def draw_gui(self, player, screen):
		for j in range(player.y_pos - 5, player.y_pos + 5):
			for i in range(player.x_pos - 5, player.x_pos + 5):
				
				component = self.get_component(j, i)

				if component == MapItems.GRASS: color = (102, 255, 102)
				elif component == MapItems.HOUSE: color = (102, 51, 0)
				elif component == MapItems.TREE: color = (0, 0, 204)
				elif component == MapItems.MONPOKE: color = (153, 0, 204)
				elif component == MapItems.PICKUP: color = (255, 255, 0)

				pygame.draw.rect(screen, color, pygame.Rect(i*20, j*20, 20, 20))
		pygame.display.update()
