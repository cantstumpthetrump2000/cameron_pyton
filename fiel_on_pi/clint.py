import socket


import time
CHUNK_SIZE = 8 * 1024
holad=""


sock = socket.socket()
sock.connect(('192.168.137.23', 12345))
chunk = sock.recv(CHUNK_SIZE)

holad=holad+(chunk.decode())
while chunk:
    chunk = sock.recv(CHUNK_SIZE)
    holad=holad+(chunk.decode())
    #print(" ")

sock.close()



import matplotlib.pyplot as plt



x_points=[]
y_points=[]

step1=holad


step2=step1.split("\n")
filter=5

filter2=10000
print("time folter set this meny second",filter2)
filter2=time.time()-filter2

print("weigth filter set to ",filter)
for q in step2[0:-1]:
    #print(q)
    y,x=q.split("-")
    #print("x")
    #print(x)
    #print("y")
    #print(y)
    try:
        x2=float(x)
        y2=float(y)
        if y2<5:
            if x2>filter2:
                x_points.append(float(x2))
                y_points.append(float(y2))
    except:
        print("error")



plt.plot(x_points,y_points)
plt.ylabel('some numbers')
plt.xlabel('some numbers')
plt.show()
