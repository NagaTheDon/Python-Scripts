# SELF: 

class Person:

	def __init__(self, name):
		self.name = name

	def say_hi(self):
		print("Hello!")

	def print_name(self):
		print("Your name is", self.name)

p = Person("")
print(p)
p.say_hi()

a = Person("Arjun")
a.print_name()



