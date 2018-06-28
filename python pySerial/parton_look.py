import serial


data=[]



with serial.Serial('COM4', 9600, timeout=1) as ser:
    for q in range(5000):
        line =ser.readline()
        x=line.decode("utf-8")
        #print(x)
        data.append(int(x))



print(data[0])

count=0
print("part 1 is over")

cont_pair=[]

for q in data:
    if q >5:
        count=0
        #print("count down")
    else:
        count=count+1
        #print("count up")

    cont_pair.append(count)

for q in range(100):
    temp=cont_pair.count(q)
    if temp >0:
        print("number of "+str(q),temp)
