import serial





with serial.Serial('COM4', 9600, timeout=5) as ser:

    line =ser.read(10000)
    print(line)
    x=line.decode("utf-8")
    print(x)
    #number= int(x[0])
    #print(number+5)
