from Flooding import *
from DVR import *
from LSR import *
from Dijkstra import *
from mongo import *
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

print('\t--- Seleccione su algoritmo ---')
print('1. Flooding')
print('2. Distance Vector')
print('3. Link State Routing')
# option = input('Ingrese algoritmo: ')
option = '1'

algorithm = None
if (option == '1'):
    algorithm = Flooding(config)
elif (option == '2'):
    algorithm = DVR(config)
else:
    algorithm = LSR(config)
    algorithm.makeTable()

'''
initialize notifications bot w/ user and password
-> listen to new message event until user option input
'''
async def initialize_bot(user, password, node=None, nodes=None, algorithm=None):
    global option
    get_notifications = Communication(user, password, node=node, nodes=nodes, algorithm=algorithm)
    get_notifications.connect(disable_starttls=True)
    get_notifications.process(forever=False)
    option = int(get_notifications.option)

'''
logged in user options
'''
def loggedInMenu():
    print('*' * 50)
    print('1. Chat privado')
    print('2. Cerrar sesion')
    print('3. Salir')
    print('-' * 50)

'''
anoymous user options
'''
def anonymousMenu():
    print('*' * 50)
    print('1. Registrar una nueva cuenta')
    print('2. Iniciar sesion')
    print('3. Salir')
    print('-' * 50)

'''
Manage user menu options
'''
async def showMenu(algorithm):
    global option
    loggedAccount = False
    sent = False
    nodes = getUsers()
    node = None

    while True:
        print('*' * 50)
        if not (loggedAccount):
            anonymousMenu()

            print('-' * 50)
            option = int(input('Ingrese la opcion: '))
            print('*' * 50)
        else:
            loggedInMenu()

            # Distance Vector 
            if (algorithm.type == 'dvr' and sent == False):
                algorithm.makeTable(node)
                start = Communication(
                    user,
                    password,
                    node=node,
                    nodes=nodes,
                    algorithm=algorithm,
                    sendMessage=True,
                    sendVector=True
                )

                # Connect to the XMPP server and start processing XMPP stanzas.
                start.connect(disable_starttls=True)
                start.process(forever=False)
                sent = True

            await initialize_bot(user, password, nodes=nodes, node=node, algorithm=algorithm)

        if not (loggedAccount):
            if (option == 1):
                print('Ingrese la informacion de la nueva cuenta')
                user = input('Username: ')
                # user = 'her19376'
                user = user+server
                password = getpass('Paswsord: ')
                # password = 'Prueba123'

                print('Registrando cuenta...')
                register = Account(
                    user,
                    password,
                    node=node,
                    register=True
                )

                # Connect to the XMPP server and start processing XMPP stanzas.
                register.connect(disable_starttls=True)
                register.process(forever=False)
                print('Cuenta registrada!')
                for item in nodes:
                    if (user == item['username']):
                        node = item['node']
            elif (option == 2):
                print('Ingrese las credenciales')
                user = input('Username: ')
                # user = 'ama19020'
                user = user+server
                password = getpass('Paswsord: ')
                # password = '12341234'

                print('Iniciando sesion...', user)
                start = Account(
                    user,
                    password,
                    node=node
                )

                # Connect to the XMPP server and start processing XMPP stanzas.
                start.connect(disable_starttls=True)
                start.process(forever=False)

                loggedAccount = start.isLoggedIn
                for item in nodes:
                    if (user == item['username']):
                        node = item['node']
            else:
                print(' ' * 20 + 'ADIOS :)' + ' ' * 20)
                print('*' * 50)
                break
        else:
            if (option == 1):
                contactToTalk = input('Usuario del contacto a mensajear: ')
                contactToTalk += server
                start = Communication(
                    user,
                    password,
                    node=node,
                    nodes=nodes,
                    algorithm=algorithm,
                    sendMessage=True,
                    contactToTalk=contactToTalk
                )

                # Connect to the XMPP server and start processing XMPP stanzas.
                start.connect(disable_starttls=True)
                start.process(forever=False)
            elif (option == 2):
                print('Cerrando sesion de ' + user + '...')
                # Disconnect
                start.disconnect()
                loggedAccount = False
            else:
                print(' ' * 20 + 'ADIOS :)' + ' ' * 20)
                print('*' * 50)
                break

if __name__ ==  '__main__':
    print('*' * 50)
    print(' ' * 17 + 'BIENVENIDO :)' + ' ' * 17)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(showMenu(algorithm))