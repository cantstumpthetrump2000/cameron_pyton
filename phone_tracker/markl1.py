import serial



myphone_mac="ec:9b:f3:5e:ec:83"
count=0
with serial.Serial('COM3', 115200, timeout=1) as ser:
    while 1 :
        line =ser.readline()

        x=line.decode("utf-8")
        if len(x)>1:
            temp=(x[27:44])
            print("temp",temp)
            if temp=="ec:9b:f3:5e:ec:83":
                print("sasmuston phone found ")
