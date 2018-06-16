import socket

CHUNK_SIZE = 8 * 1024
holad=""


sock = socket.socket()
sock.connect(('192.168.1.156', 12345))
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

for q in step2[0:-1]:
    print(q)
    y,x=q.split("-")
    x_points.append(float(x))
    y_points.append(float(y))






plt.plot(x_points,y_points)
plt.ylabel('some numbers')
plt.xlabel('some numbers')
plt.show()
