from Constants import *
from InventoryItem import *
from Map import *
from MonPoke import *
from Player import *


def convert_list(list, end=''):
	out = ''
	for item in list:
		out += str(item) + end
	return out

player = Player()
map = Map()

while True:
	print("\033c", end="")

	map.draw_map(player)
	print(f'\n\n---------CAPTURED----------\n{convert_list(player.captured_monpokes)}')
	print('---------INVENTORY---------')
	print(convert_list(player.inventory))
	move = input().lower()
	new_x, new_y = player.x_pos, player.y_pos

	if move == 'w':
		new_y -= 1
	elif move == 's':
		new_y += 1
	elif move == 'a':
		new_x -= 1
	elif move == 'd':
		new_x += 1
	elif move == 'use':
		print("\033c", end="")
		choice = input()

	if map.map_components[(new_y, new_x)] != MapItems.GRASS:
		continue
	player.x_pos, player.y_pos = new_x, new_y
