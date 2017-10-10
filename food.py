class Food(object):

	minimum_calories = 0
	is_edible = True

	def __init__(self):
		self.water_content = 0
		self.name = 'food'
		self.calories = None

	def printName(self):
		print "I'm "+ self.name

class Fruit(Food):
	
	def __init__(self, name, calories, sweet):
		Food.__init__(self)
		self.name = name
		self.calories = calories
		self.sweet = sweet


	
