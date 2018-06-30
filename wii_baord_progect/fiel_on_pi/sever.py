


import socket

CHUNK_SIZE = 8 * 1024

server_socket = socket.socket()
host = '192.168.1.156'
server_socket.bind((host, 12345))
server_socket.listen(5)
while True:
    client_socket, addr = server_socket.accept()
    with open('weight data', 'rb') as f:
        data = f.read(CHUNK_SIZE)
        while data:
            client_socket.send(data)
            data = f.read(CHUNK_SIZE)
    client_socket.close()
