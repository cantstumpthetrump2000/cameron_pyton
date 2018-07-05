import serial



start=[1,1,1]

end=[1,0,1]


data=[]

with serial.Serial('COM8', 9600, timeout=1) as ser:
    for q in range(20):
        line =ser.readline()
        x=line.decode("utf-8")
        #print(x)
        try:
            data.append(int(x))
        except:
            print("bad input ",q)





print("part 1 is over")


out_put_data=[]






start_found=True
for q in range(len(start)):
    #print("start vaule ",start[q])
    #print("data  vaule ",data[q])
    if data[q] !=start[q]:
        start_found=False
        print("not a match")

if start_found==True:
    print("Start found")


count=1

end_found=False
while start_found==True:
    count=count+1




    #print("start vaule ",end[q])
    #print("data  vaule ",data[q])
    if data[count:count+3] ==end:
        end_found=True



    if end_found==True:
        start_found=False
        end_found=False
    else:
        print("count",count)
        out_put_data.append(data[count])

print(out_put_data)
