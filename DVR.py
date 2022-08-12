from dijkstar import Graph, find_path

class DVR:
	def __init__(self, config) :
		self.config = config
	
	def Dijkstra(self):
		graph = Graph()
		for key, value in self.config.items():
			for val in value:
				graph.add_edge(key, val, 1)
		print(find_path(graph, 'A', 'C'))