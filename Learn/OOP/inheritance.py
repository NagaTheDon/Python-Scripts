#OOP allow use to reuse the code. 
# Inheritance can be imagined as type and sub-type relationship between classes

# Suppose you have two classes like students and teachers 
# They have somethings that are in common like name, age and address

# Some specific characterstics like salary, courses and leaves for teachers
# Some specific characterstics like marks and fees for students. 

# Create two independent classes for each type and process them
# adding a new COMMON characterstic would mean adding to both classes. 

#A best way to make a common class with all the common variables and INHERIT
# from them

class SchoolMember:

	def __init__(self, name, age):
		self.name = name
		self.age = age
		print("{} created".format(self.name))

	def get_details(self):
		print("Name: {} Age: {}".format(self.name, self.age))

class Teacher(SchoolMember):

	def __init__(self, name, age, salary):
		SchoolMember.__init__(self,name,age)
		self.salary = salary
		print("Teacher created : {}".format(self.name))

	def tell(self):
		SchoolMember.get_details(self)
		print("Salary : ",self.salary)

class Student(SchoolMember):
	def __init__(self,name, age,fees):
		SchoolMember.__init__(self,name,age)
		self.fees = fees
		print("Student created : {}".format(self.name))

	def tell(self):
		SchoolMember.get_details(self)
		print("Fees : ",self.fees)

t = Teacher("Cook",29,1200)
s = Student("Arjun",21,1500)

members = [t,s]

for member in members:
	member.tell()