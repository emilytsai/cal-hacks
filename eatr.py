# Cal Hacks Fall 2015
# Name: Cal Hacks Team EATR
# Author: Annie Tsai

"""The EATR module implements the input and output of the grocery list."""


from datetime import date

################
# Core Classes #
################


class Place:
	"""A Place that holds grocery items."""

	def __init__(self, name):
		"""Create a Place with the given name to store the grocery
		items passed in.

		name -- A string; the name of the location storing the items.
		"""
		self.name = name
		self.groceries = []

	def add_groceryitem(self, groceryitem):
		"""Add a GroceryItem to this Place."""
		self.groceries.append(groceryitem)

	def remove_groceryitem(self, groceryitem):
		"""Remove a GroceryItem from this Place."""
		if groceryitem.life <= 0:
			groceryitem.warning()
		self.groceries.remove(groceryitem)


class Refrigerator(Place):
	"""A Refrigerator holds grocery items."""

	name = 'Refrigerator'


class GroceryList(Place):
	"""A GroceryList contains items that have not yet been bought."""

	name = 'Grocery List'


class GroceryItem:
	"""A GroceryItem that is in a Place."""

	def __init__(self, name, life, date):
		"""Create a GroceryItem with the given name.

		name -- A string; the name of this GroceryItem.
		life -- An integer; the approximate number of days this GroceryItem
		can last.
		date -- A date represented in 
		"""
		self.name = name
		self.life = life
		self.date = date # need to find a way to select date in proper format

	def check_life(self):
		if self.life <= 0:
			self.warning()
		elif 0 < self.life < 4:
			self.urgent()
		else:
			self.update()

	def countdown(self):
		self.life -= 1

	def update(self):
		return "Your " + self.name + " is still good for " + life + "days!"

	def urgent(self):
		return "Cook your " + self.name + " soon! It may only be good for "
			+ self.life " more days!"

	def warning(self):
		return "Cook your " + self.name + " today to ensure freshness!"


class Cabbage(GroceryItem):

	name = 'Cabbage'
	life = 14

	def get_info(self):
		return "Cabbage usually stays fresh for about 1-2 weeks but can last \
			anywhere from 3 weeks to up to 2 months when properly stored! Pro tip: \
			Do not wash your cabbage until you are ready to use it. Keep it \
			tightly bagged."

