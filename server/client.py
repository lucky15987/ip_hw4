import socket





client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Client: Socket Created')

host = 'localhost'
port = 5432

num = input('Enter a number between 0-10: ')
n = str.encode(num)

try:
    client_socket.sendto(n, ('localhost', 5432))

    data2, addr = client_socket.recvfrom(1024)
    print(data2.decode())

    data3, addr = client_socket.recvfrom(1024)
    print(data3.decode())

    client_socket.sendto("Thanks bro!".encode(), addr)
    print('Message Sent to Server')

finally:
    print("Closing Client")
    client_socket.close()
