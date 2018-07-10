import serial
import threading
import time

main_data=[]
class myThread (threading.Thread):
   def __init__(self, threadID, name, port_to_use):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.port_to_use = port_to_use

   def run(self):
      print ("Starting " + self.name)
      print_time(self.name, 5, self.port_to_use)
      print ("Exiting " + self.name)

def print_time(threadName, _, port_to_use):

    port=serial.Serial(port_to_use,115200, timeout=3)
    data_packet=[]
    mark=True
    while mark:
        line =port.readline()
        #print(line)
        x=line.decode("utf-8")
        print(threadName)
        print(x)
        main_data[int(threadName)].append((x,threadName))
        mark=False
    #print("#############")
    #print(port_to_use)
    #print(x)
    #print("#############")
    port.close()



from serial.tools import list_ports
list_of_ports=list_ports.comports()



port_to_skip=["COM1"]

port_to_use=[]

for  current_port in list_of_ports:
    data_flow=current_port[0]

    if data_flow in port_to_skip:
        print("skipping port",data_flow)
        continue
    print("try to open port ",data_flow)

    try:

        print("opening port")
        port=serial.Serial(data_flow, 115200, timeout=3)

        print("reading line")
        line =port.readline()

        print("decodeing")
        x=line.decode("utf-8")

        print("pirnt data")
        print(x)
        print("breacking conection")
        port.close()
        port_to_use.append(data_flow)


    except Exception as inst:
        print("can't open port ",data_flow)






print("port to use ",port_to_use)








# Create new threads
therd_array=[]

for q in port_to_use:
    main_data.append([])
    therd_array.append(myThread(len(therd_array),len(therd_array),q))


for q in therd_array:
    q.start()
#thread1.start()
#thread2.start()

print ("Exiting Main Thread")


for t in therd_array:
    t.join()


for q in main_data:
    print(q)

print("done ")
