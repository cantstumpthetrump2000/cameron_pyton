import serial


y_points=[]



with serial.Serial('COM4', 9600, timeout=1) as ser:
    for q in range(20000):
        line =ser.readline()
        x=line.decode("utf-8")
        #print(x)
        y_points.append(int(x))


import matplotlib.pyplot as plt

x_points=[]
for q in range(len(y_points)):
    x_points.append(q)




plt.plot(x_points,y_points)
plt.ylabel('some numbers')
plt.xlabel('some numbers')
plt.show()
