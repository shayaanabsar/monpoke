from Constants import *

class InventoryItem:

	def __init__(self, type_, health=100):
		self.type_ = type_
		self.health = health

	def __str__(self):
		if self.type_ == InventoryTypes.BAGUETTE:
			return '🥖'