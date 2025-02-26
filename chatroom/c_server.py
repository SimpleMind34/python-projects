import socket
import threading

host = '127.0.0.1'
port = 59000

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((host,port))

server.listen()

clients = []
aliases = []

def broadcast(message):
  # if isinstance(message, str):
  #       message = message.encode('utf-8') 
  for client in clients:
    client.send(message)

def handle_client(client):
  while True:
    try:
      message = client.recv(1024)
      broadcast(message)
    except:
      index = clients.index(client)
      clients.remove(client)
      client.close()
      alias = aliases[index]
      broadcast(f'{alias} has left the chat room!'.encode('utf-8'))
      aliases.remove(alias)
      break

# main function to receive the clients connections

def receive():
  while True:
    print("The server is running and listening... ")
    client,address = server.accept()
    print(f'connection established with {str(address)}')
    message = 'what is your alias?'
    client.send(message.encode())
    alias = client.recv(1024).decode('utf-8')
    aliases.append(alias)
    clients.append(client)
    print(f'The alias of this client is {alias}')
    broadcast(f'{alias} has connected to the chat room'.encode())
    client.send('\nYou have connected successfully\n'.encode('utf-8'))
    # handling clients via threads
    thread = threading.Thread(target=handle_client,args = (client,))
    thread.start()

if __name__ == "__main__":
  receive()




