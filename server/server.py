import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #takes IP4 address and using UDP networking
print('Server: Socket Created')

host = 'localhost'
port = 5432

server_socket.bind((host, port))    #bind to address

print('Server: Socket conneted to ' + host)

#server_socket.listen(3)  #generate a listener for 3 connections (clients) TCP networking only
print('Waiting for connections')


while True:   
    data, addr = server_socket.recvfrom(1024)
    print('Connected with', addr)
    print('Message: ', data.decode())

    if data:
        server_socket.sendto("I got your message".encode(), addr)
        print('Message Sent')

    data2, addr = server_socket.recvfrom(1024)
    print('Message 2: ', data2.decode())

    server_socket.close()
