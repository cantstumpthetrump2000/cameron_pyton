import socket
s=socket.socket()
host=socket.gethostbyname("thepiratebay.asia")
print(host)
port=80
s.connect((host,port))
data_get="GET /\r\n"
data_get=data_get.encode()

s.send(data_get)

val = s.recv(10000)
# Split off the HTTP headers
val=val.decode()
print(val)
