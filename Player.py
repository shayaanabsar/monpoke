from Constants import *
from InventoryItem import *
from MonPoke import *

class Player:

	def __init__(self, x_pos=0, y_pos=0, health=100):
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.health = health
		self.captured_monpokes = [CapturedMonPoke(MonPokeTypes.SHOHAM)]
		self.inventory = [InventoryItem(InventoryTypes.BAGUETTE)]

	def add_item(self, item):
		self.inventory.append(item)
		print(f"{item} added to {self.name}'s inventory.")

	def use_item(self, item, target, number):
		if item in self.inventory:
			print(f"{self.name} uses {item} on {target} {number} time(s)")
			self.inventory[item].health -= number
		else:
			print(f"{self.name}'s inventory does not contrain {item}.'")

