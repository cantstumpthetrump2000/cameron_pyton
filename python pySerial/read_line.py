import serial





with serial('COM4', 46800, timeout=1) as ser:

    line =ser.readline()
    print(line)
    x=line.decode("utf-8")
    print(x)
    #number= int(x[0])
    #print(number+5)
