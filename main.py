from Flooding import *
from DVR import *
from LSR import *
import json
from dijkstar import Graph, find_path

def read_input(name: str) -> dict:
	file = open(name, 'r')
	data = file.read()
	data = data.replace('\'', '\"')
	json_data = json.loads(data)
	return json_data['config']

config: dict = read_input('topologia.txt')

dvr = DVR(config)
dvr.Dijkstra()