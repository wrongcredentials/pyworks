
class Card():
	def __init__(self, value, suit):
		self._value = value
		self._suit = suit

	def value(self):
		return value

	#Magick Methods:	
	def __lt__(self, other):
		return self._value < other._value

	def __gt__(self, other):
		return self._value > other._value

print(Card(1,2) < Card(2,1))


#Класс - родитель
class GeometryObject():
	def __init__(self, x, y):
		self._x = x
		self._y = y

	def __lt__(self, other):
		return self.square() < other.square

#Класс - потомок
class Square(GeometryObject):
	def __init__(self, x, y, width, height):
		super().__init__(x,y)
		self._w = width
		self._h =height

	def square(self):
		return (self._w) * (self._h)

class Circle(GeometryObject):
	def __init__(self, x, y, radius):
		super().__init__(x,y)
		self._r = radius

	def square(self):
		return 6.28


sq = Square(1, 2, 4, 5)

print(sq._square())