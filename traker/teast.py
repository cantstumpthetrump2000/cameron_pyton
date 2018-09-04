import serial
import threading
import time



#thered definion
#main_count=[]
class myThread (threading.Thread):
    def __init__(self, threadID, name, port_to_use):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.port_to_use = port_to_use
      self.therd_data=5
      self.mark=True

    def run(self):
      print ("Starting " + self.name)
      self.print_time(self.name, 5, self.port_to_use)
      print ("Exiting " + self.name)

    def print_time(self,threadName, _, port_to_use):

        port=serial.Serial(port_to_use,115200, timeout=3)
        data_packet=[]

        while self.mark:
            line =port.readline()
            #print(line)
            x=line.decode("utf-8")
            #print("data from usb port",threadName)
            print("teast ",x,threadName)
            #print("")
            try:
                self.therd_data=float(x)
            except:
                pass
        #print("#############")
        #print(port_to_use)
        #print(x)
        #print("#############")
        port.close()


#scaning
port_to_use=[]
port_to_skip=["COM1"]

from serial.tools import list_ports
list_of_ports=list_ports.comports()

print("all port found")
for q in list_of_ports:
    print(q)
for  current_port in list_of_ports:
    data_flow=current_port[0]

    if data_flow in port_to_skip:
        print("skipping port",data_flow)
        continue


    try:
        print("try to open port ",data_flow)
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
        port_to_use.append(data_flow)
        print("port is useable ")
    except Exception as inst:
        print("can't open port ",data_flow)
        print (type(inst))
        print (inst.args)
        print (inst)
        print()
















thead_list=[]
output_data=[]
if len(port_to_use)<3:
    print("not enough seons are conects")
    exit()

for vaule in port_to_use:

    thead_list.append( myThread(1, str(vaule),vaule))
    output_data.append([])


for q in thead_list:
    q.start()

print("list of all thered runing")
for q in (thead_list):
    print(q.name)

import pygame
import time

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)



gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('teaxt demo')
clock = pygame.time.Clock()




def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text,postion):
    largeText = pygame.font.Font('freesansbold.ttf',50)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (postion)
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()








gameExit = False

while not gameExit:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()




    gameDisplay.fill(white)
    couuuuu=1
    for q in (thead_list):
        print(q.therd_data-5)
        #message_display("hello",(150*couuuuu,300))
        message_display(str(q.therd_data),(150*couuuuu,300))
        couuuuu=couuuuu+1
    pygame.display.update()
    clock.tick(60)


pygame.quit()
quit()
















while 1:
    print("teast_loop",teast_loop)




print ("Exiting Main Thread")
exit()
