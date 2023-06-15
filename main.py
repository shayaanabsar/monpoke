from random import choices, randint, choice
from enum import Enum

class MapItems(Enum):
	GRASS = 1
	HOUSE = 2
	TREE = 3
	MONPOKE = 4

class MonPokeTypes(Enum):
	SHOHAM = 1
	IBSID = 2
	SHAYAAN = 3
	CJEYS = 4
	SOHAM = 5
	ZAC = 6
	SUDANSHU = 7
	SAMEER = 8
	ARYAN  = 9
	DAVID  = 10
	ALI    = 11
	DMILS  = 12
	RBROWN = 13

def generate_map_component():
	return choices(list(MapItems), weights=(90, 2, 3, 1), k=1)[0]

def generate_monpoke_type():
	return choices(list(MonPokeTypes), weights=(13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1), k=1)[0]

def convert_list(list):
	out = ''
	for item in list: out += str(item)
	return out
	
class Player:
	def __init__(self, x_pos=0, y_pos=0, health=100):
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.health = health
		self.captured_monpokes = [CapturedMonPoke(MonPokeTypes.SHOHAM)]
		self.inventory = []

class CapturedMonPoke:
	def __init__(self, type_, health=100):
		self.type = type_
		self.health = 100

	def __str__(self):
		if self.type == MonPokeTypes.SHOHAM:
			return '🍥'
		elif self.type == MonPokeTypes.IBSID:
			return '🦝'
		elif self.type == MonPokeTypes.SHAYAAN:
			return '🦧'
		elif self.type == MonPokeTypes.CJEYS:
			return '🐫'
		elif self.type == MonPokeTypes.SOHAM:
			return '🐿️'
		elif self.type == MonPokeTypes.ZAC:
			return '🦩'
		elif self.type == MonPokeTypes.SUDANSHU:
			return '🦗'
		elif self.type == MonPokeTypes.SAMEER:
			return '🦏'
		elif self.type == MonPokeTypes.ARYAN:
			return '🦨'
		elif self.type == MonPokeTypes.DAVID:
			return '🐊'
		elif self.type == MonPokeTypes.ALI:
			return '🦑'
		elif self.type == MonPokeTypes.DMILS:
			return '🐉'
		elif self.type == MonPokeTypes.RBROWN:
			return '🦖'
			
class MonPoke(CapturedMonPoke):
	def __init__(self, type_, x_pos, y_pos, health=100):
		super().__init__(type_, health)
		self.x_pos = x_pos
		self.y_pos = y_pos


class Map:
	def __init__(self):
		self.map_components = {}
		self.monpokes = {}

	def draw_map(self, player):
		for j in range(player.y_pos-5, player.y_pos+5):
			for i in range(player.x_pos-5, player.x_pos+5):
				if (player.y_pos, player.x_pos) == (j, i):
					print('🧕', end='')
				else:
					if (j, i) not in self.map_components:
						self.map_components[(j, i)] = generate_map_component()

						if self.map_components[(j, i)] == MapItems.MONPOKE:
							type_ = generate_monpoke_type()
							monpoke = MonPoke(type_, j, i)
							self.monpokes[(j, i)] = monpoke
					
					if self.map_components[(j, i)] == MapItems.GRASS:
						print('🟥', end='')
					elif self.map_components[(j, i)] == MapItems.HOUSE:
						print('🏠', end='')
					elif self.map_components[(j, i)] == MapItems.TREE:
						print('🌳', end='')
					elif self.map_components[(j, i)] == MapItems.MONPOKE:
						print(self.monpokes[(j, i)], end='')

			print('')

		
		print(f'\n\nCaptured MonPokes: {convert_list(player.captured_monpokes)}')

#pokemon

player = Player()
map = Map()

while True:
	print("\033c", end="")

	map.draw_map(player)

	move = input()
	new_x, new_y = player.x_pos, player.y_pos

	if move == 'w':
		new_y -= 1
	elif move == 's':
		new_y += 1
	elif move == 'a':
		new_x -= 1
	elif move == 'd':
		new_x += 1

	if map.map_components[(new_y, new_x)] != MapItems.GRASS:
		continue
	player.x_pos, player.y_pos = new_x, new_y
	