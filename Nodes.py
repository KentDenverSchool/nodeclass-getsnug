class Node:
	nextNodes = null
	def __init__(self, newData, pointer):
		self.pointer = pointer
		self.data = newData
test = Node("hello", [None])
print(test.pointer)


