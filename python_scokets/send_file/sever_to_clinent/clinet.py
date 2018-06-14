import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.1.172'
port = 50008

s.connect((host,port))

def ts():

    data_from_sever = s.recv(1024).decode()
    print (data_from_sever)

ts()

s.close ()
