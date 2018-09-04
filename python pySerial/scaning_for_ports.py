import serial


from serial.tools import list_ports
list_of_ports=list_ports.comports()



port_to_skip=["COM1"]


for  current_port in list_of_ports:
    data_flow=current_port[0]

    if data_flow in port_to_skip:
        print("skipping port",data_flow)
        continue
        print("try to open port ",data_flow)

    try:
        while 1:
            port_loacl=data_flow
            print("opening port")
            port=serial.Serial(data_flow, 115200, timeout=3)

            print("reading line")
            line =port.readline()

            print("decodeing")
            x=line.decode("utf-8")

            print("breacking conection")
            port.close()

            print("data")
            print(x[0:-2])
            #print()
            if len(x)<1:
                print("emputey data given closing port ",port_loacl)
                break


    except Exception as inst:
        print("can't open port ",data_flow)
        print (type(inst))
        print (inst.args)
        print (inst)
        print()
