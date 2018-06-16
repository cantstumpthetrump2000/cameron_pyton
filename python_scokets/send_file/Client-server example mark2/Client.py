import socket

CHUNK_SIZE = 8 * 1024
holad=""


sock = socket.socket()
sock.connect(('localhost', 12345))
chunk = sock.recv(CHUNK_SIZE)

holad=holad+(chunk.decode())
while chunk:
    chunk = sock.recv(CHUNK_SIZE)
    holad=holad+(chunk.decode())
    #print(" ")

sock.close()


print(holad)
