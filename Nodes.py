class Node:
	def __init__(self, newData, pointer):
		self.pointer = pointer
		self.data = newData
	def getData(self):
		return self.data
	def changeData(self, data):
		self.data = data
	def addNode(self, newNode):
		self.pointer.append(newNode)
	def rmNode(self, index):
		del self.pointer[index]
	def getXNode(self, index):
		if(index<len(pointer)):
			return pointer[index]
trunk = Node("Main", [None])
students = Node("Students", [None])
freshman = Node("Freshman", [None])
sophomores = Node("Sophomores", [None])
juniors = Node("Juniors", [None])
seniors = Node("Seniors", [None])
people = [Node("Person 1", [None]), Node("Person 2", [None]), Node("Person 3", [None]), Node("Person 4", [None]), Node("Person 5", [None]),
Node("Person 6", [None]), Node("Person 7", [None]), Node("Person 8", [None]), Node("Person 9", [None]), Node("Person 10", [None]),
Node("Person 11", [None]), Node("Person 12", [None]), Node("Person 13", [None]), Node("Person 14", [None]), Node("Person 15", [None]),
Node("Person 16", [None])]
trunk.addNode(students)
students.addNode(freshman)
students.addNode(sophomores)
students.addNode(juniors)
students.addNode(seniors)
i = 0;
for item in people:
	if(i<4):
		freshman.addNode(item)
		i+=1
	elif(i<8):
		sophomores.addNode(item)
		i+=1
	elif(i<12):
		juniors.addNode(item)
		i+=1
	elif(i<16):
		seniors.addNode(item)
		i+=1
students.rmNode(0)
for year in students.pointer:
	year.rmNode(0)
for student in juniors.pointer:
	print(student.getData())


