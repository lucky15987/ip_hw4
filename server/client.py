import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Client: Socket Created')

host = 'localhost'
port = 1234

msg = "Test Succesful"

client_socket.sendto(msg.encode(), ('localhost', 5432))



client_socket.close