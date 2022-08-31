from Dijkstra import *

from dijkstar import Graph, find_path
class LSR:
	def __init__(self, config):
		self.type = 'lsr'
		self.config = config
		self.nodes = list(config.keys())
		self.graph = Dijkstra(config)

	def makeTable(self):
		self.table = {}
		for start in self.nodes:
			self.graph = Dijkstra(self.config)
			previous_nodes, shortest_path = self.graph.dijkstra_algorithm(start)
			for finish in self.nodes:
				path, cost = self.graph.get_result(previous_nodes, shortest_path, start, finish)
				self.table[(start, finish)] = path, cost