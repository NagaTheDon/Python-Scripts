# Polymorphism is an important feature that is used when you have 
# commonly named methods across classes or subclasses

class Shark():

    def swim(self):
        print("The shark is swimming")

    def swim_backwards(self):
        print("The shark cannot swim swim_backwards")

    def skeleton(self):
        print("The shark skeleton is made of cartilage")

    def number(self, fish):
    	self.value = 

class Clownfish():
    def swim(self):
        print("The clownfish is swimming.")

    def swim_backwards(self):
        print("The clownfish can swim backwards.")

    def skeleton(self):
        print("The clownfish's skeleton is made of bone.")

sammy = Shark()
sammy.skeleton()

casey = Clownfish()
casey.skeleton()