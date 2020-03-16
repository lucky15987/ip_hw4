import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Server: Socket Created')

host = 'localhost'
port = 5432

server_socket.bind((host, port)) #ip address of the host's current pc/device
print('Server: Socket conneted to ' + host)

server_socket.listen(0)  #generate a listener for connection

while True:
    n = server_socket.recvfrom(2040)

