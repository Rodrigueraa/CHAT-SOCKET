#cliente

from socket import *

host = gethostname()
port = 12000

client = socket(AF_INET, SOCK_STREAM)
client.connect((host, port))
print('CLIENTE: ')
terminado = False
print('Digite tt para terminar o chat')

while not terminado:
    client.send(input('You: ').encode('utf-8'))
    msg = client.recv(1024).decode('utf-8')
    if msg == 'tt':
        terminado = True
        client.close()
    else: 
        print('Stranger: ', msg)

client.close()
