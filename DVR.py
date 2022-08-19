from dijkstar import Graph, find_path

class DVR:
	def __init__(self, config, node):
		self.node = node
		self.config = config[node]
		self.nodes = list(config.keys())
		self.table = {}

	def makeTable(self):
		self.vector = {}
		for node in self.nodes:
			if (self.node == node):
				self.vector[(node, node)] = [node, 0]
			elif (node in self.config):
				self.vector[(self.node, node)] = [node, 1]
			else:
				self.vector[(self.node, node)] = [node, 9999]
	
	def updateVector(self, origin, vector):
		distance =	self.vector[(self.node, origin)][1]
		changeCount = 0
		for node in self.nodes:
			if ((origin == node) or (self.node == node)): continue

			# Makes the change if direct move > indirect move
			if (self.vector[(self.node, node)][1] > vector[(origin, node)][1] + distance):
				self.vector[(self.node, node)] = [origin, vector[(origin, node)][1] + distance]
				changeCount += 1
		self.table[self.node] = self.vector.copy()
		self.table[origin] = vector.copy()
		print(self.table)
		return changeCount