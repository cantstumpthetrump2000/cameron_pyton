import serial
import threading
import time


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

    port=serial.Serial(port_to_use, 9600, timeout=3)
    data_packet=[]
    mark=True
    while mark:
        line =port.readline()
        #print(line)
        x=line.decode("utf-8")

        data_packet.append(x)

        if "end" in x :
            print(threadName)
            for q in data_packet:
                print(q)

            break

    #print("#############")
    #print(port_to_use)
    #print(x)
    #print("#############")
    port.close()


# Create new threads
thread1 = myThread(1, "Thread-1", "COM5")
thread2 = myThread(2, "Thread-2", "COM8")

# Start new Threads
thread1.start()
thread2.start()

print ("Exiting Main Thread")
