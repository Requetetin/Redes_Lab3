from pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb+srv://root:root@redes.da5gpu9.mongodb.net/?retryWrites=true&w=majority")
users = client['redes']['users']

def getUsers():
  documents = users.find({})
  temp = []
  for document in documents:
    temp.append(document)
  return temp

def insertUsers(data):
  users.insert_many(data)

def deleteAllUsers():
  users.delete_many({})

if __name__ ==  '__main__':
  nodes = [
    { 'node': 'A', 'username': 'ama19357@alumchat.fun' },
    { 'node': 'B', 'username': 'ama19020@alumchat.fun' },
    { 'node': 'C', 'username': 'her19376@alumchat.fun' },
  ]

  print('---> Limpiando base de datos')
  deleteAllUsers()
  print('---> Base de datos limpiada')

  print('---> Agregando a los usuarios')
  insertUsers(nodes)
  print('---> Usuarios agregados')

  pprint(getUsers())