from Flooding import *
from DVR import *
from LSR import *
import json

SERVER = 'alumchact.fun'

def read_input(name: str) -> dict:
	file = open(name, 'r')
	data = file.read()
	data = data.replace('\'', '\"')
	json_data = json.loads(data)
	return json_data['config']
config: dict = read_input('topologia.txt')

# username = input('Ingrese su usuario: ') + '@' + SERVER
# password = input('Ingrese su contraseña: ')
# node = input('Ingrese el ID de su nodo: ')

# print('\t--- Seleccione su algoritmo ---')
# print('1. Flooding')
# print('2. Distance Vector')
# print('3. Link State Routing')
# algorithm = input('Ingrese algoritmo: ')

dvr = DVR(config, 'B')
dvr2 = DVR(config, 'C')
dvr.makeTable()
dvr2.makeTable()
dvr.updateVector('C', dvr2.vector)
