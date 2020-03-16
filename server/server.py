import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Server: Socket Created')

host = 'localhost'
port = 5432

server_socket.bind((host, port)) #ip address of the host's current pc/device
print('Server: Socket conneted to ' + host)

server_socket.listen(3)  #generate a listener for 3 connections (clients)
print('Waiting for connections')

while True:
    client_socket, addr = server_socket.accept()
    print('Connected with ', addr)

    n = server_socket.recvfrom(2040)

    server_socket.close()
