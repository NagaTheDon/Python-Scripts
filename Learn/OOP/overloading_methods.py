class Vector:
	def __init__(self,x,y):
		self.x = x 
		self.y = y

	def __str__(self):
		return "String of Vector  (%d, %d)" % (self.x , self.y)

	def __add__(self,other):
		return Vector(self.x + other.x, self.y + other.y)

v1 = Vector(2, 10)
v2 = Vector(2, 10)
v3 = Vector(3, 29)

print(v1)

print(v1+v2+v3)

#Output
#======
# String of Vector  (2, 10)
# String of Vector  (4, 20)