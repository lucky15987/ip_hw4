import socket
import math


def factorial(n):
    return str(math.factorial(n))


server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # takes IP4 address and using UDP networking
print('Server: Socket Created')

host = 'localhost'
port = 5432

server_socket.bind((host, port))  # bind to address

print('Server: Socket connected to ' + host)

print('Waiting for connections')

while True:
    try:
        data, addr = server_socket.recvfrom(1024)
        n = int(data.decode())
        print('Connected with', addr)
        print('The number (n) received was: ', n)
        print('')

        if data:
            server_socket.sendto("The Server received this number (n): ".encode() + data, addr)

            server_socket.sendto("The factorial of ".encode() + data + " is: ".encode() + factorial(n).encode(), addr)
            #print(factorial(n))
            print('Message sent to Client\n')

        data2, addr = server_socket.recvfrom(1024)
        print('Message from Client: ', data2.decode())
    finally:
        print('Server still waiting for more connections')
        #server_socket.close()
