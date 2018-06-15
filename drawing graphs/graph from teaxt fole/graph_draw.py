import matplotlib.pyplot as plt



x_points=[]
y_points=[]

file=open("data-file","r")

step1=file.read()


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
