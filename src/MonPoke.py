from Constants import *
from random import randint, choice

class CapturedMonPoke:
	def __init__(self, type_, health=100):
		self.type_ = type_
		self.health = health

	def fight(self):
		option = ''
		while option not in ('BIG', 'SMALL'):
			option = input('Enter Attack Option: ').upper()
#options are
		#BIG, SMALL, HEAL, RUN
		
		if option == 'BIG':
			self.health -= randint(5, 7)
			hit  = randint(7, 10)
		elif option == 'SMALL':
			self.health -= randint(1, 3)
			hit = randint(3, 5)

		return hit

	def __str__(self):
		if self.type_ == MonPokeTypes.SHOHAM:
			return '🍥'
		elif self.type_ == MonPokeTypes.IBSID:
			return '🦝'
		elif self.type_ == MonPokeTypes.SHAYAAN:
			return '🦧'
		elif self.type_ == MonPokeTypes.CJEYS:
			return '🐫'
		elif self.type_ == MonPokeTypes.SOHAM:
			return '🐫'
		elif self.type_ == MonPokeTypes.ZAC:
			return '🦩'
		elif self.type_ == MonPokeTypes.SUDANSHU:
			return '🦗'
		elif self.type_ == MonPokeTypes.SAMEER:
			return '🦏'
		elif self.type_ == MonPokeTypes.ARYAN:
			return '🦨'
		elif self.type_ == MonPokeTypes.DAVID:
			return '🐊'
		elif self.type_ == MonPokeTypes.ALI:
			return '🦑'
		elif self.type_ == MonPokeTypes.DMILS:
			return '🐉'
		elif self.type_ == MonPokeTypes.RBROWN:
			return '🦖'


class MonPoke(CapturedMonPoke):

	def __init__(self, type_, x_pos, y_pos, health=100):
		super().__init__(type_, health)
		self.x_pos = x_pos
		self.y_pos = y_pos

	def fight(self):
		option = choice(['BIG', 'SMALL'])
		
		if option == 'BIG':
			self.health -= randint(5, 7)
			hit  = randint(7, 10)
		elif option == 'SMALL':
			self.health -= randint(1, 3)
			hit = randint(3, 5)

		return hit