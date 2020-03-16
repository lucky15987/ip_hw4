import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Client: Socket Created')

host = 'localhost'
port = 5432

#client_socket.connect((host, port))

msg = "Test Succesful"

try:
    client_socket.sendto(msg.encode(), ('localhost', 5432))

    data2, addr = client_socket.recvfrom(1024)
    print('Message Recieved: ', data2.decode())
    client_socket.sendto("Thanks bro!".encode(), addr)
    print('Message Sent to Server!')

finally:
    print("Closing Client")
    client_socket.close()
