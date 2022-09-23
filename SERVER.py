#servidor

from socket import *


host = gethostname()
port = 55551

print(f'INFORMAÇOES DO SERVIDOR-> \nHOST: {host}, PORT {port} \n')

server = socket(AF_INET, SOCK_D)
server.bind((host, port))
server.listen()
client, end = server.accept()

terminado = False
while not terminado:
    msg = client.recv(1024).decode('utf-8')
    if msg == 'tt':
        terminado = True
        server.close()
    else:
        print('Stranger: ', msg)
        client.send(input('You: ').encode('utf-8'))

client.close()
server.close()

