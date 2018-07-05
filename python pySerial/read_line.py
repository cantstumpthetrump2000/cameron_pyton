import serial





with serial.Serial('COM8', 9600, timeout=2) as ser:

    line =ser.readline()
    print(line)
    x=line.decode("utf-8")
    print(x)
    #number= int(x[0])
    #print(number+5)
