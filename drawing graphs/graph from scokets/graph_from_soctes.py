import matplotlib.pyplot as plt



import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.137.133'
port = 50008
try:
    s.connect((host,port))
except:
    print("serve is not conectible ")
    exit()


data_from_sever = s.recv(1024).decode()
#print (data_from_sever)



s.close ()







x_points=[]
y_points=[]



step1=data_from_sever


step2=step1.split("\n")

for q in step2[1:-1]:
    print(q)
    y,x=q.split("-")
    x_points.append(float(x))
    y_points.append(float(y))






plt.plot(x_points,y_points)
plt.ylabel('some numbers')
plt.xlabel('some numbers')
plt.show()
