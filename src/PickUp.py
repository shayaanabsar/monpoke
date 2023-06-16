from Constants import *

class PickUp:

	def __init__(self, type_, health=100):
		self.type_ = type_
		self.health = health

	def __str__(self):
		if self.type_ == PickUpTypes.BAGUETTE:
			return '🥖'
		elif self.type_ == PickUpTypes.BURGER:
			return '🍔'
		elif self.type_ == PickUpTypes.PIZZA:
			return '🍕'
		elif self.type_ == PickUpTypes.PRETZEL:
			return '🥨'
		elif self.type_ == PickUpTypes.DOUGHNUT:
			return '🍩'

	def use_pickup(self):
		if self.type_ == PickUpTypes.BAGUETTE:
			return 10
		elif self.type_ == PickUpTypes.BURGER:
			return 20
		elif self.type_ == PickUpTypes.PIZZA:
			return 30
		elif self.type_ == PickUpTypes.PRETZEL:
			return 40
		elif self.type_ == PickUpTypes.DOUGHNUT:
			return 50