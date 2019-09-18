import random


class IntGen():
	@classmethod
	def generate(cls, min_val, max_val):
		return random.randrange(min_val, max_val)
