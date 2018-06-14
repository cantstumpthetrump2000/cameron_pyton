import matplotlib.pyplot as plt
import random
import time

x_points=[]
y_points=[]


start_time=time.time()

start_weight=110
for q in range(10):
    x_points.append(start_time)
    y_points.append(start_weight)

    start_time=start_time+random.randint





plt.plot(x_points,y_points)
plt.ylabel('some numbers')
plt.xlabel('some numbers')
plt.show()
