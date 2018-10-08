import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.16.10.1'

port =27036
print("runign")

s.connect((host,port))


data_from_sever = s.recv(1024).decode()
print ("data from server ",data_from_sever)



s.close ()
