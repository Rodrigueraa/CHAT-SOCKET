from socket import *
import threading

host = gethostname()
port = 12000

print(f'INFORMAÇOES DO SERVIDOR-> \nHOST: {host}, PORT {port} \n')

def receive(client_socket):
    while True:
        try:
            msg = client_socket.recv(1024).decode('utf-8')
            if not msg:
              break
            print(msg)
        except ConnectionResetError:
            break

def send(client_socket):
    while True:
        msg = input()
        if msg == 'tt':
            client_socket.send(msg.encode('utf-8'))
            break
        client_socket.send(msg.encode('utf-8'))


server = socket(AF_INET, SOCK_STREAM)
server.bind(('', port))
server.listen()

while 1:
    client_socket, client_address = server.accept()
    print(f'Conectado com {client_address}')
    recv_thread = threading.Thread(target=receive, args=(client_socket,))
    recv_thread.start()

    send_thread = threading.Thread(target=send, args=(client_socket,))
    send_thread.start()

client_socket.close()
server.close()

