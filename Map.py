from Constants import *
from MonPoke import *
from random import choices

def generate_map_component():
	return choices(list(MapItems), weights=(90, 2, 3, 1), k=1)[0]


def generate_monpoke_type():
	return choices(list(MonPokeTypes),
	               weights=(13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1),
	               k=1)[0]


class Map:

	def __init__(self):
		self.map_components = {(0, 0): MapItems.GRASS}
		self.monpokes = {}

	def draw_map(self, player):
		for j in range(player.y_pos - 5, player.y_pos + 5):
			for i in range(player.x_pos - 5, player.x_pos + 5):
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
