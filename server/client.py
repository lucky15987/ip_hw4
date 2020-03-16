import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Client: Socket Created')

host = 'localhost'
port = 1234

msg = "Test Succesful"

try:
    client_socket.sendto(msg.encode(), ('localhost', 5432))

    data2 = client_socket.recvfrom(1024)
    print('Message Recieved: ', data2.decode())

finally:
    print("Closing Client")
    client_socket.close()
