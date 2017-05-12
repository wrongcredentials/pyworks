class Person:
	def __init__(self):
		self.name = "vasya"
		self.age = 28

	def get_name(self):
		return self.name

	def get_age(self):
		return self.age

p = Person()
p.get_name()
