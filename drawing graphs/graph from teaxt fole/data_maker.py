
import random
import time

x_points=[]
y_points=[]
#weight then time

start_time=time.time()
start_weight=110
number_of_points=10

for q in range(number_of_points):
    x_points.append(start_time)
    y_points.append(start_weight)

    start_time=start_time+random.randint(1,20)
    start_weight=start_weight+random.randint(-5,2)

file=open("data-file","w")


for q in range(number_of_points):
    data_to_wite=(str(y_points[q])+"-"+str(x_points[q])+"\n")

    file.write(data_to_wite)

file.close()
