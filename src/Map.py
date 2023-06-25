from Constants import *
from MonPoke import *
from random import choices
from PickUp import *
import pygame

def generate_map_component():
	return choices(list(MapItems), weights=(30, 30, 30, 30, 2, 3, 1, 1), k=1)[0]


def generate_monpoke_type():
	return choices(list(MonPokeTypes),
	               weights=(3, 2, 1),
	               k=1)[0]

def generate_pickup_type():
	return choices(list(PickUpTypes),
	               weights=(5, 4, 3, 2, 1),
	               k=1)[0]
class Map:

	def __init__(self):
		self.map_components = {(0, 0): MapItems.GRASS_1}
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
					
					if component in (MapItems.GRASS_1, MapItems.GRASS_2, MapItems.GRASS_3, MapItems.GRASS_4): print('🟩', end='')
					elif component == MapItems.TREE: print('🌳', end='')
					elif component == MapItems.MONPOKE: print(self.monpokes[(j, i)], end='')
					elif component == MapItems.FLOWER: print('🌷', end='')
					elif component == MapItems.PICKUP: print(self.pickups[(j, i)], end='')

			print('')

	def blit_image(self, screen, j, i, x_coord, y_coord):
		if self.map_components[(j, i)] == MapItems.GRASS_1: img_path = 'monpoke/src/icons/grass/Grass 1.png'
		elif self.map_components[(j, i)] == MapItems.GRASS_2: img_path = 'monpoke/src/icons/grass/Grass 2.png'
		elif self.map_components[(j, i)] == MapItems.GRASS_3: img_path = 'monpoke/src/icons/grass/Grass 3.png'
		elif self.map_components[(j, i)] == MapItems.GRASS_4: img_path = 'monpoke/src/icons/grass/Grass 4.png'
		elif self.map_components[(j, i)] == MapItems.TREE: img_path = 'monpoke/src/icons/misc/Tree.png'
		elif self.map_components[(j, i)] == MapItems.FLOWER: img_path = 'monpoke/src/icons/misc/Flower.png'

		img = pygame.image.load(img_path).convert_alpha()
		img = pygame.transform.scale(img, (50, 50))
		screen.blit(img, (x_coord*50, y_coord*50))
			
	def draw_gui(self, player, screen):
		y_coord, x_coord = 0, 0
		for j in range(player.y_pos-5, player.y_pos+5):
				x_coord = 0
				for i in range(player.x_pos-5, player.x_pos+5):
					img_path = None
		
					if (player.y_pos, player.x_pos) == (j, i):
						player.blit_image(screen, x_coord, y_coord)
					else:
						component = self.get_component(j, i)
	
						if self.map_components[(j, i)]  == MapItems.PICKUP:
							self.pickups[(j, i)].blit_image(screen, x_coord, y_coord)
						elif self.map_components[(j, i)]  == MapItems.MONPOKE:
							self.monpokes[(j, i)].blit_image(screen, x_coord, y_coord)
						else: 
							self.blit_image(screen, j, i, x_coord, y_coord)
			
		
					x_coord += 1
				y_coord += 1
		