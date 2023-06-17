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

class Game:
	def __init__(self):
		self.player = Player()
		self.map = Map()
		self.message = ''


	def battle(self, new_x, new_y):
		if self.player.captured_monpokes[0].health <= 0:
			self.message = 'Current MonPoke doesn\'t have enough health.'
		else:
			while True:
				print("\033c", end="")
				print('---------BATTLE---------\n\n')
				print(f'You : {str(self.player.captured_monpokes[0])}. Health: {self.player.captured_monpokes[0].health}')
				print(f'Them: {str(self.map.monpokes[(new_y, new_x)])}. Health: {self.map.monpokes[(new_y, new_x)].health}')
				self.map.monpokes[(new_y, new_x)].health -= self.player.fight()
				
				if self.map.monpokes[(new_y, new_x)].health  <= 0 or self.player.captured_monpokes[0].health <= 0:
					break
					
				self.player.captured_monpokes[0].health -= self.map.monpokes[(new_y, new_x)].fight()
				
				if self.player.captured_monpokes[0].health <= 0 or self.map.monpokes[(new_y, new_x)].health  <= 0:
					break
					
			self.map.monpokes[(new_y, new_x)].health = max(0, self.map.monpokes[(new_y, new_x)].health)
			self.player.captured_monpokes[0].health = max(0, self.player.captured_monpokes[0].health)
			
			if self.map.monpokes[(new_y, new_x)].health <= self.player.captured_monpokes[0].health:
				self.message = 'MonPoke Captured!'
				captured_monpoke = CapturedMonPoke(self.map.monpokes[(new_y, new_x)].type_, health=self.map.monpokes[(new_y, new_x)].health)
				self.player.captured_monpokes.appendleft(captured_monpoke)
				del self.map.monpokes[(new_y, new_x)]
				self.map.map_components[(new_y, new_x)] = MapItems.GRASS
			else:
				self.message = 'You Lost!'


	def pickup(self, new_x, new_y):
		self.player.inventory.append(self.map.pickups[(new_y, new_x)])
		del self.map.pickups[(new_y, new_x)]
		self.map.map_components[(new_y, new_x)] = MapItems.GRASS

	def handle_input(self):
		move = input().lower()
		new_x, new_y = self.player.x_pos, self.player.y_pos
	
		if move == 'w':
			new_y -= 1
		elif move == 's':
			new_y += 1
		elif move == 'a':
			new_x -= 1
		elif move == 'd':
			new_x += 1
		elif move == 'use':
			self.player.use_pickups()

		if self.map.map_components[(new_y, new_x)] == MapItems.MONPOKE:
			self.battle(new_x, new_y)
		elif self.map.map_components[(new_y, new_x)] == MapItems.PICKUP:
			self.pickup(new_x, new_y)
		if self.map.map_components[(new_y, new_x)] != MapItems.GRASS:
			return
			
		self.player.x_pos, self.player.y_pos = new_x, new_y

	def play(self):
		while True:
			print("\033c", end="")
			self.map.draw_map(self.player)
			print(f'\n{self.message}')
			print(f'\n---------CAPTURED----------\n{convert_list(self.player.captured_monpokes, health=True)}')
			print('---------INVENTORY---------')
			print(convert_list(self.player.inventory))
			
			self.handle_input()