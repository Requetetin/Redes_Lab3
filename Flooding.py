class Flooding:
  def __init__(self, config) :
    self.type = 'fld'
    self.config = config
    self.nodes = list(config.keys())
    self.visited = dict.fromkeys(self.nodes, False)
    self.sent = dict.fromkeys(self.nodes, False)
    self.route = {}

  def transmit(self, current , origin = None):
    if self.visited[current] == False:
      self.route[current] = []
      for node in self.config[current]:
        if node == origin:
          pass
        else:
          self.route[current].append(node)
          print(current, ',', node)
          self.visited[current] = True
          self.transmit(node, origin=current)
  
  def resetSent(self):
    self.sent = dict.fromkeys(self.nodes, False)