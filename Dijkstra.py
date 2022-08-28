import sys

class Dijkstra(object):
	def __init__(self, config):
		self.nodes = list(config.keys())
		self.graph = {}

		for node in self.nodes:
			self.graph[node] = {}
	
		for key, value in config.items():
			for val in value:
				self.add_edge(key, val, 1)
    
	def add_edge(self, u, v, weight):
		self.graph[u][v] = weight
		self.graph[v][u] = weight
    
	def get_outgoing_edges(self, node):
		connections = []
		for out_node in self.nodes:
			if self.graph[node].get(out_node, False) != False:
				connections.append(out_node)
		return connections
    
	def value(self, node1, node2):
		return self.graph[node1][node2]

	def dijkstra_algorithm(self, start_node):
		unvisited_nodes = self.nodes
	
		# We'll use this dict to save the cost of visiting each node and update it as we move along the graph   
		shortest_path = {}
	
		# We'll use this dict to save the shortest known path to a node found so far
		previous_nodes = {}
	
		# We'll use max_value to initialize the "infinity" value of the unvisited nodes   
		max_value = sys.maxsize
		for node in unvisited_nodes:
			shortest_path[node] = max_value
		# However, we initialize the starting node's value with 0   
		shortest_path[start_node] = 0
		
		# The algorithm executes until we visit all nodes
		while unvisited_nodes:
			# The code block below finds the node with the lowest score
			current_min_node = None
			for node in unvisited_nodes: # Iterate over the nodes
				if current_min_node == None:
					current_min_node = node
				elif shortest_path[node] < shortest_path[current_min_node]:
					current_min_node = node
					
			# The code block below retrieves the current node's neighbors and updates their distances
			neighbors = self.get_outgoing_edges(current_min_node)
			for neighbor in neighbors:
				tentative_value = shortest_path[current_min_node] + self.value(current_min_node, neighbor)
				if tentative_value < shortest_path[neighbor]:
					shortest_path[neighbor] = tentative_value
					# We also update the best path to the current node
					previous_nodes[neighbor] = current_min_node
	
			# After visiting its neighbors, we mark the node as "visited"
			unvisited_nodes.remove(current_min_node)
		
		return previous_nodes, shortest_path

	def get_result(self, previous_nodes, shortest_path, start_node, target_node):
		path = []
		node = target_node
		
		while node != start_node:
			path.append(node)
			node = previous_nodes[node]
	
		# Add the start node manually
		path.append(start_node)
		
		path.reverse()
		# print("Valor de", start_node, "->", target_node, ":", shortest_path[target_node])
		# print(path)
		return [path, shortest_path[target_node]]