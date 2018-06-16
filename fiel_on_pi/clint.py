import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.1.156'
port = 50008
try:
    s.connect((host,port))
except:
    print("serve is not conectible ")
    exit()

def ts():
    while 1:
        data_from_sever = s.recv(1024).decode()
        print("data got",data_from_sever)
        print()
        if "done" in  data_from_sever:
            break


ts()

s.close ()
