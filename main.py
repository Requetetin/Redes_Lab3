from Flooding import *
from DVR import *
from LSR import *
from Dijkstra import *
from accountFunc import *
from communicationFunc import *

import json
from getpass4 import getpass
import asyncio
import nest_asyncio
nest_asyncio.apply()

server = "@alumchat.fun"
option = 0

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

# dvr = DVR(config, 'B')
# dvr2 = DVR(config, 'C')
# dvr.makeTable()
# dvr2.makeTable()
# dvr.updateVector('C', dvr2.vector)

lsr = LSR(config)
lsr.makeTable()
print(lsr.table)

# flooding = Flooding(config, 'B')
# flooding.transmit('A')



# '''
# initialize notifications bot w/ user and password
# -> listen to new message event until user option input
# '''
# async def initialize_bot(user, password):
#     global option
#     get_notifications = Communication(user, password)
#     get_notifications.connect()
#     get_notifications.process(forever=False)
#     option = int(get_notifications.option)

# '''
# logged in user options
# '''
# def loggedInMenu():
#     print('*' * 50)
#     print('1. Chat privado')
#     print('2. Chat grupal')
#     print('3. Cerrar sesion')
#     print('4. Salir')
#     print('-' * 50)

# '''
# anoymous user options
# '''
# def anonymousMenu():
#     print('*' * 50)
#     print('1. Registrar una nueva cuenta')
#     print('2. Iniciar sesion')
#     print('3. Salir')
#     print('-' * 50)

# '''
# Manage user menu options
# '''
# async def showMenu():
#     global option
#     loggedAccount = False

#     while True:
#         print('*' * 50)
#         if not (loggedAccount):
#             anonymousMenu()

#             print('-' * 50)
#             option = int(input('Ingrese la opcion: '))
#             print('*' * 50)
#         else:
#             loggedInMenu()
#             await initialize_bot(user, password)

#         if not (loggedAccount ):
#             if (option == 1):
#                 print('Ingrese la informacion de la nueva cuenta')
#                 user = input('Username: ')
#                 user = user+server
#                 password = getpass('Paswsord: ')

#                 print('Registrando cuenta...')
#                 register = Account(user, password, register=True)

#                 # Connect to the XMPP server and start processing XMPP stanzas.
#                 register.connect()
#                 register.process(forever=False)
#                 print('Cuenta registrada!')
#             elif (option == 2):
#                 print('Ingrese las credenciales')
#                 user = input('Username: ')
#                 user = user+server
#                 password = getpass('Password: ')

#                 print('Iniciando sesion...', user)
#                 start = Account(user, password)

#                 # Connect to the XMPP server and start processing XMPP stanzas.
#                 start.connect()
#                 start.process(forever=False)

#                 loggedAccount = start.isLoggedIn
#             else:
#                 print(' ' * 20 + 'ADIOS :)' + ' ' * 20)
#                 print('*' * 50)
#                 break
#         else:
#             if (option == 1):
#                 contactToTalk = input('Usuario del contacto a mensajear: ')
#                 contactToTalk += server
#                 start = Communication(user, password, sendMessage=True, contactToTalk=contactToTalk)
#                 # Connect to the XMPP server and start processing XMPP stanzas.
#                 start.connect()
#                 start.process(forever=False)
#             elif (option == 2):
#                 contactToTalk = input('Room a mensajear: ')
#                 contactToTalk += muc_server
#                 start = Communication(user, password, room=contactToTalk)
#                 # Connect to the XMPP server and start processing XMPP stanzas.
#                 start.connect()
#                 start.process(forever=False)
#             elif (option == 3):
#                 print('Cerrando sesion de ' + user + '...')
#                 # Disconnect
#                 start.disconnect()
#                 loggedAccount = False
#             else:
#                 print(' ' * 20 + 'ADIOS :)' + ' ' * 20)
#                 print('*' * 50)
#                 break


# if __name__ ==  '__main__':
#     print('*' * 50)
#     print(' ' * 17 + 'BIENVENIDO :)' + ' ' * 17)

#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(showMenu())