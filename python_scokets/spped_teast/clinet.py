import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.1.172'
port = 50008

s.connect((host,port))

def ts(data_to_send):

   data_to_send=str(data_to_send)

   try:
       s.send(data_to_send.encode())
   except:
       print("send fail host down")
       exit()
   data_from_sever = s.recv(1024).decode()
   print (data_from_sever)


for q in range(1000000):
   ts(q)

s.close ()
