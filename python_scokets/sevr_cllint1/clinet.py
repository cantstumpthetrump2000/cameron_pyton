import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 50008

s.connect((host,port))

def ts(data_to_send):

   data_to_send=str(data_to_send)


   s.send(data_to_send.encode())

   data_from_sever = s.recv(1024).decode()
   print (data_from_sever)

while 1:
   r = input('enter')
   ts(r)

s.close ()
