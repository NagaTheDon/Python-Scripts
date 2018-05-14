#Namespaces : Names are valid within the context of these classes and objects

# Class Variables - These are shared
#				  - Can be accessed by all instances of that class
# 				  - Only one copy of class variable 
#						-> One object can change to a class variable and can be seen on all the other instances

class droid:

	#Class variable:

	population  = 0

	def __init__(self, name):
		#Object variabkes
		self.name = name

		print("Initialising {}".format(self.name))

		droid.population += 1


	def die(self):
		print("{} droid is destroyed!".format(self.name))

		droid.population -= 1

		if(droid.population == 0):
			print("All droids destroyed")

		else:
			print("Remaining robots are {}".format(droid.population))


	def say_hi(self):
		print("I'm {}".format(self.name))


	@classmethod
	# This is a wrapper. This is a function that wraps around another function
	#  so that it can do something before or after the inner function
	def how_many_1(cls):
		print("We have {} droids - 2!".format(cls.population))

	def how_many_2(self):
		print("We have {} droids - 2!".format(droid.population))


droid1 = droid("R2-D2")
droid1.say_hi()
droid.how_many_1()
droid1.how_many_2() # Error: Have not sent a name. Hence, won't construct

droid2 = droid("C-3PO")
droid2.say_hi()
droid.how_many_1()
droid2.how_many_2()

print("droids can work here!")

droid1.die()
droid2.die()

droid.how_many_1()


