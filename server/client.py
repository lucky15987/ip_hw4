import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Client: Socket Created')

host = 'localhost'
port = 1234


try:
    print()

finally:
    print('Client: Closing Socket')
    client_socket.close