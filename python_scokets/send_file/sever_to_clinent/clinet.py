import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.137.133'
port = 50008
try:
    s.connect((host,port))
except:
    print("serve is not conectible ")
    exit()

def ts():

    data_from_sever = s.recv(1024).decode()
    print (data_from_sever)

ts()

s.close ()
