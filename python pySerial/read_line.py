import serial





with serial.Serial('COM4', 9600, timeout=1) as ser:

    line =ser.readline()
    x=line.decode("utf-8")
    print(x[0])
    number= int(x[0])
    print(number+5)
