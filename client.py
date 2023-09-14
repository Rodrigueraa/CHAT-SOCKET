from socket import *
import threading

host = gethostname()
port = 12000

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


client = socket(AF_INET, SOCK_STREAM)
client.connect((host, port))
print('CLIENTE: ')

recv_thread = threading.Thread(target=receive, args=(client,))
recv_thread.start()

send_thread = threading.Thread(target=send, args=(client,))
send_thread.start()

