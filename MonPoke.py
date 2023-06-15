from Constants import *

class CapturedMonPoke:
	def __init__(self, type_, health=100):
		self.type_ = type_
		self.health = 100

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
			return '🐿️'
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