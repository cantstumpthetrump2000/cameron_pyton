#!/usr/bin/python

import threading



main_data=5
class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print ("Starting " + self.name)
      function()
      print ("Exiting " + self.name)



def function():
    while 1:
        global main_data
        main_data=int(input("cahnge the number"))




# Create new threads
thread1 = myThread(1, "Thread-1", 1)


# Start new Threads
thread1.start()


print ("Exiting Main Thread")
while 1:

    print(main_data)
