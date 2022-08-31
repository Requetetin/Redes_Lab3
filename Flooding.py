class Flooding:
  def __init__(self, config) :
    self.type = 'fld'
    self.config = config
    self.nodes = list(config.keys())
    self.visited = dict.fromkeys(self.nodes, False)

  def transmit(self, current , origin = None):
    if self.visited[current] == False: 
      for node in self.config[current]:
        if node == origin:
          pass
        else:
          print(current, ',', node)
          self.visited[current] = True
          self.transmit(node, origin=current)