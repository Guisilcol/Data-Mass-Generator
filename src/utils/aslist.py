
class ASList:
	"""
	Array-set List: A wrapper of list and set.
	
	by HermesPasser
	"""
	def __init__(self, values=[], unique=False):
		self._is_unique = unique
		self._list = set() if unique else []
		self.update(values)
	
	def __str__(self):
		return str(self._list)
	
	def __len__(self):
		return len(self._list)
	
	def __iter__(self):
		return iter(self._list)
	
	def add(self, item):
		"""Insert object"""
		if self._is_unique:
			self._list.add(item)
		else:
			self._list.append(item)
	
	def remove(self, item):
		"""Remove item"""
		self._list.remove(item)
	
	def update(self, itens):
		"""Append elements from the iterable to the list"""
		if self._is_unique:
			self._list.update(itens)
		else:
			self._list.extend(itens)
	
	def pop(self):
		"""Remove and return item at the end of the list"""
		return self._list.pop()
		
	def rand_pop(self):
		"""Pop a random element and return it"""
		import random
		if self._is_unique:
			val = random.sample(self._list, 1)[0]
			self._list.remove(val)
		else:
			idx = random.randrange(len(self._list))
			val = self._list[idx]
			del self._list[idx]
		return val
	
	def rand_item(self):
		"""Return a random element"""
		import random
		return random.sample(self._list, 1)[0]
	
