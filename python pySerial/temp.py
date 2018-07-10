import serial



fire=open("data_log basen","w")

with serial.Serial('COM10', 9600, timeout=2) as ser:
    while 1 :
        line =ser.readline()
        try:
            print(line)
            x=line.decode("utf-8")
            print(x)
            #number= int(x[0])
            #print(number+5)
            fire.write(x)
        except:
            print("error")
fire.close()
