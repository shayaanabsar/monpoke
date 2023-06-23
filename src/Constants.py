from enum import Enum



class Directions(Enum):
	UP = 1
	DOWN = 2
	LEFT = 3
	RIGHT = 4

class PickUpTypes(Enum):
	BAGUETTE = 1
	APPLE = 2
	CABBAGE = 3
	CAKE = 4
	CHICKEN = 5

class MapItems(Enum):
	GRASS_1 = 1
	GRASS_2 = 2
	GRASS_3 = 3
	GRASS_4 = 4
	TREE = 5
	FLOWER = 6
	MONPOKE = 7
	PICKUP = 8


class MonPokeTypes(Enum):
	SLIME_BALL = 1
	GIRAFFE = 2
	HEDGEHOG = 3