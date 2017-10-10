class Food(object):
	
	def __init__(self, name, calories):
		self.name = name
		self.calories = calories


class Fruit(Food):
	
	def __init__(self, name, calories, fiber):
		Food.__init__(self, name, calories)
		self.sweet = True
		self.fiber = fiber

class Meat(Food):

	def __init__(self, name, calories, protein):
		Food.__init__(self, name, calories)
		self.sweet = False
		self.flavor = protein
	
