from dijkstar import Graph, find_path
class LSR:
	def __init__(self, config):
		self.config = config
		self.nodes = list(config.keys())
		self.graph = Graph()
		for key, value in self.config.items():
			for val in value:
				self.graph.add_edge(key, val, 1)

	def makeTable(self):
		self.table = {}
		for start in self.nodes:
			for finish in self.nodes:
				nodes, _, _, total_costs = find_path(self.graph, start, finish)
				self.table[(start, finish)] = [nodes, total_costs]