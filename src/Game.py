from Constants import *
from Map import *
from MonPoke import *
from Player import *
from PickUp import *
from time import sleep
import pygame
import pygame.freetype
from pygame.locals import QUIT


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
				self.map.map_components[(new_y, new_x)] = MapItems.GRASS_1
			else:
				self.message = 'You Lost!'


	def pickup(self, new_x, new_y):
		self.player.inventory[self.map.pickups[(new_y, new_x)].type_] += 1
		del self.map.pickups[(new_y, new_x)]
		self.map.map_components[(new_y, new_x)] = MapItems.GRASS_1

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
		if self.map.map_components[(new_y, new_x)] not in (MapItems.GRASS_1, MapItems.GRASS_2, MapItems.GRASS_3, MapItems.GRASS_4):
			return
			
		self.player.x_pos, self.player.y_pos = new_x, new_y

	def battle_gui(self, screen, new_x, new_y):
		img = pygame.image.load('monpoke/src/icons/Battle Arena.png').convert_alpha()
		font = pygame.font.Font("monpoke/src/font.ttf", 15)
		big_text_rect = pygame.Rect(80, 300, 100, 30)
		small_text_rect = pygame.Rect(200, 300, 100, 30)
		print(self.player.captured_monpokes[0].health)
		if self.player.captured_monpokes[0].health <= 0:
			self.message = 'Not enough health.'
			return
		else:
			while True:
				screen.blit(img, (0, 0))
				self.player.captured_monpokes[0].blit_image(screen, 3, 4)
				screen.blit(font.render(str(self.player.captured_monpokes[0].health), 0, (255, 255, 255)), (150, 250))
				
				self.map.monpokes[(new_y, new_x)].blit_image(screen, 10, 4)
				screen.blit(font.render(str(self.map.monpokes[(new_y,new_x)].health), 0, (255, 255, 255)), (500, 250))
					
				screen.blit(font.render('BIG', 0, (255, 255, 255)), (80, 300))
				screen.blit(font.render('SMALL', 0, (255, 255, 255)), (200, 300))
	
				for event in pygame.event.get():
					if event.type == QUIT:
						pygame.quit()
						sys.exit()
					elif event.type == pygame.locals.MOUSEBUTTONDOWN:
						if event.button == 1:
							mouse_pos = pygame.mouse.get_pos()
							if big_text_rect.collidepoint(mouse_pos):
								self.map.monpokes[(new_y, new_x)].health -= self.player.captured_monpokes[0].big_attack()
							elif small_text_rect.collidepoint(mouse_pos):
								self.map.monpokes[(new_y, new_x)].health -= self.player.captured_monpokes[0].small_attack()
	
			
							self.player.captured_monpokes[0].health -= self.map.monpokes[(new_y, new_x)].fight()
	
				if self.map.monpokes[(new_y, new_x)].health  <= 0 or self.player.captured_monpokes[0].health <= 0:
					break
				pygame.display.update()
			
					
				
		self.map.monpokes[(new_y, new_x)].health = max(0, self.map.monpokes[(new_y, new_x)].health)
		self.player.captured_monpokes[0].health = max(0, self.player.captured_monpokes[0].health)
		if self.map.monpokes[(new_y, new_x)].health <= self.player.captured_monpokes[0].health:
			self.message = 'MonPoke Captured!'
			captured_monpoke = CapturedMonPoke(self.map.monpokes[(new_y, new_x)].type_, health=self.map.monpokes[(new_y, new_x)].health)
			self.player.captured_monpokes.appendleft(captured_monpoke)
			del self.map.monpokes[(new_y, new_x)]
			self.map.map_components[(new_y, new_x)] = MapItems.GRASS_1
		else:
			self.message = 'You Lost!'

	def play(self):
		while True:
			print("\033c", end="")
			self.map.draw_map(self.player)
			print(f'\n{self.message}')
			print(f'\n---------CAPTURED----------\n{convert_list(self.player.captured_monpokes, health=True)}')
			print('---------INVENTORY---------')
			print(convert_list(self.player.inventory))
			
			self.handle_input()

	def play_gui(self):
		pygame.init()
		screen = pygame.display.set_mode((755, 500))
		font = pygame.font.Font("monpoke/src/font.ttf", 15)
		pygame.display.set_caption('MonPoke')
		use_pickups_rect = pygame.Rect(505, 150, 100, 30)
		
		while True:
			screen.fill((178, 190, 181))
			screen.blit(font.render("INVENTORY-", 0, (255, 255, 255)), (505, 10))
			screen.blit(font.render("MONPOKES-", 0, (255, 255, 255)), (505, 250))
			screen.blit(font.render(self.message, 0, (255, 255, 255)), (505, 450))
			screen.blit(font.render('USE PICKUPS', 0, (255, 255, 255)), (505, 150))
			self.player.blit_inventory(screen)
			self.player.blit_monpokes(screen)
			
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
				elif event.type == pygame.KEYDOWN:
					new_x, new_y, new_facing = self.player.x_pos, self.player.y_pos, self.player.direction
		
					if event.key == pygame.K_UP:
						new_y -= 1
						new_facing = Directions.UP
					elif event.key == pygame.K_DOWN:
						new_y += 1
						new_facing = Directions.DOWN
					elif event.key == pygame.K_LEFT:
						new_x -= 1
						new_facing = Directions.LEFT
					elif event.key == pygame.K_RIGHT:
						new_x += 1
						new_facing = Directions.RIGHT
					
					if self.map.map_components[(new_y, new_x)] == MapItems.PICKUP:
						self.pickup(new_x, new_y)
					elif self.map.map_components[(new_y, new_x)] == MapItems.MONPOKE:
						print((new_y, new_x) in self.map.monpokes)
						self.battle_gui(screen, new_x, new_y)
					if self.map.map_components[(new_y, new_x)] not in (MapItems.GRASS_1, MapItems.GRASS_2, MapItems.GRASS_3, MapItems.GRASS_4):
						continue

					self.player.x_pos, self.player.y_pos = new_x, new_y
					self.player.direction = new_facing
				elif event.type == pygame.locals.MOUSEBUTTONDOWN:
					if event.button == 1:
						mouse_pos = pygame.mouse.get_pos()
						if use_pickups_rect.collidepoint(mouse_pos):
							self.player.use_pickups()
			self.map.draw_gui(self.player, screen)
			pygame.display.update()
			
			print("\033c", end="")
			self.map.draw_map(self.player)		
		