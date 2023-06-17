from Constants import *
from PickUp import *
from MonPoke import *
from copy import copy
from collections import deque

class Player:

	def __init__(self, x_pos=0, y_pos=0, health=100):
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.health = health
		self.captured_monpokes = deque([CapturedMonPoke(MonPokeTypes.SHOHAM)])
		self.inventory = [PickUp(PickUpTypes.BAGUETTE)]

	def fight(self):
		return self.captured_monpokes[0].fight()
			
	def use_pickups(self):
		for i, pickup in enumerate(self.inventory):
			for j, monpoke in enumerate(self.captured_monpokes):
				self.captured_monpokes[j].health = min(100, self.captured_monpokes[j].health+pickup.use_pickup())
				
		self.inventory = []
			

	def use_item(self, item, target, number):
		if item in self.inventory:
			print(f"{self.name} uses {item} on {target} {number} time(s)")
			self.inventory[item].health -= number
		else:
			print(f"{self.name}'s inventory does not contrain {item}.'")

