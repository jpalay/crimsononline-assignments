class HashableList(list):
	def __hash__(self):
		return reduce(lambda a, x: a + str(x), self, "").__hash__()