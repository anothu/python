from random import randint

class Die():

	def __init__(self,num_sides=6):
		#🎲有六个面
		self.num_sides = num_sides

	def roll(self):
		return randint(1,self.num_sides)

