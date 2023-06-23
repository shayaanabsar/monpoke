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
		self.captured_monpokes = deque()
		self.inventory = {item: 0 for item in list(PickUpTypes)}
		self.direction = Directions.DOWN

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

	def blit_inventory(self, screen):
		font = pygame.font.Font("monpoke/src/font.ttf", 15)

		x_coord, y_coord = 10, 1
		for item in self.inventory:
			if self.inventory[item] > 0:
				PickUp(item).blit_image(screen, x_coord, y_coord, no_background=True)
				screen.blit(font.render(str(self.inventory[item]), 0, (255, 255, 255)), (x_coord*50, (y_coord+1)*50))
				x_coord += 1
		print(self.inventory)
	def blit_image(self, screen, x_coord, y_coord):
		if self.direction == Directions.LEFT:
			img_path = 'monpoke/src/icons/player/Player Left.png'
		elif self.direction == Directions.RIGHT:
			img_path = 'monpoke/src/icons/player/Player Right.png'
		elif self.direction == Directions.DOWN:
			img_path = 'monpoke/src/icons/player/Player Down.png'
		elif self.direction == Directions.UP:
			img_path = 'monpoke/src/icons/player/Player Up.png'

		img = pygame.image.load(img_path).convert_alpha()
		img = pygame.transform.scale(img, (50, 50))
		screen.blit(img, (x_coord*50, y_coord*50))