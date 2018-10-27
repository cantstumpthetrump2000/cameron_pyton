import socket


tageget_ip="192.168.137.72"
port=80
MESSAGE = b"Hello, World!"
#MESSAGE=MESSAGE.encode()
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.sendto(MESSAGE,(tageget_ip,port))
#
