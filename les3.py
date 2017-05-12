class Person:
	def __init__(self):
		self.name = "vasya"
		self.age = 28

	def __str__(self):
		return "Name: {}, Age: {}".format(self.name, self.age)

	def get_name(self):
		return self.name

	def set_name(self):
		self.name = name

	def get_age(self):
		return self.age

p = Person()
p.get_name()

p2 = Person()
p2.set_name("petya")
p2.get.name()


class Person2:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def get_name(self):
		return self.name

	def set_name(self):
		self.name = name

	def get_age(self):
		return self.age

p = Person2()
p.get_name("vasya", 28)