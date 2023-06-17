from Constants import *
from Map import *
from MonPoke import *
from Player import *
from PickUp import *
from time import sleep
def convert_list(list, health=False):
	out = ''
	for item in list:
		out += str(item)
		if health: out += f'({item.health})'
		out += ' '
	return out

player = Player()
map = Map()
message = ''

while True:
	print("\033c", end="")

	map.draw_map(player)
	print(f'\n{message}')
	print(f'\n---------CAPTURED----------\n{convert_list(player.captured_monpokes, health=True)}')
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
		player.use_pickups()

	if map.map_components[(new_y, new_x)] == MapItems.MONPOKE:
		if player.captured_monpokes[0].health <= 0:
			message = 'Current MonPoke doesn\'t have enough health.'
		else:
			while True:
				print("\033c", end="")
				print('---------BATTLE---------\n\n')
				print(f'You : {str(player.captured_monpokes[0])}. Health: {player.captured_monpokes[0].health}')
				print(f'Them: {str(map.monpokes[(new_y, new_x)])}. Health: {map.monpokes[(new_y, new_x)].health}')
				map.monpokes[(new_y, new_x)].health -= player.fight()

				if map.monpokes[(new_y, new_x)].health  <= 0:
					break
					
				player.captured_monpokes[0].health -= map.monpokes[(new_y, new_x)].fight()
				
				if player.captured_monpokes[0].health <= 0:
					break
		
			map.monpokes[(new_y, new_x)].health = max(0, map.monpokes[(new_y, new_x)].health)
			player.captured_monpokes[0].health = max(0, player.captured_monpokes[0].health)
			
			if map.monpokes[(new_y, new_x)].health < player.captured_monpokes[0].health:
				message = 'MonPoke Captured!'
				captured_monpoke = CapturedMonPoke(map.monpokes[(new_y, new_x)].type_, health=map.monpokes[(new_y, new_x)].health)
				player.captured_monpokes.appendleft(captured_monpoke)
				del map.monpokes[(new_y, new_x)]
				map.map_components[(new_y, new_x)] = MapItems.GRASS
			else:
				message = f'You Lost!'
				
				
		
	elif map.map_components[(new_y, new_x)] == MapItems.PICKUP:
		player.inventory.append(map.pickups[(new_y, new_x)])
		del map.pickups[(new_y, new_x)]
		map.map_components[(new_y, new_x)] = MapItems.GRASS
	if map.map_components[(new_y, new_x)] != MapItems.GRASS:
		continue
	player.x_pos, player.y_pos = new_x, new_y
