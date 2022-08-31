import json
class DVR:
	def __init__(self, config):
		self.type = 'dvr'
		self.config = config
		self.nodes = list(config.keys())
		self.neighbours = []
		self.table = {}

	def getKey(self, origin, destination):
		return str(origin) + '-' + str(destination)

	def makeTable(self, node):
		self.config = self.config[node]
		self.node = node
		self.vector = {}
		for node in self.nodes:
			if (self.node == node):
				self.vector[self.getKey(node, node)] = [node, 0]
			elif (node in self.config):
				self.vector[self.getKey(self.node, node)] = [node, 1]
				self.neighbours.append(node)
			else:
				self.vector[self.getKey(self.node, node)] = [node, 9999]
	
	def updateVector(self, origin, vector):
		distance =	self.vector[self.getKey(self.node, origin)][1]
		changeCount = 0
		print(self.vector)
		for node in self.nodes:
			if ((origin == node) or (self.node == node)): continue

			# Makes the change if direct move > indirect move
			if (self.vector[self.getKey(self.node, node)][1] > vector[self.getKey(origin, node)][1] + distance):
				self.vector[self.getKey(self.node, node)] = [origin, vector[self.getKey(origin, node)][1] + distance]
				changeCount += 1
		self.table[self.node] = self.vector.copy()
		self.table[origin] = vector.copy()
		print(self.vector)
		return changeCount

	def getMessage(self):
		return str(self.vector)
	
	def toDic(self, vector):
		return json.loads(vector.replace("'", '"'))