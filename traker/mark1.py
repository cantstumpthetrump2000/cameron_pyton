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
            if  not "scan" in x  and not"networks" in x and len(x)>2:
                print("goinf in",threadName)
                #print(x,threadName)
                self.therd_data=(10000*(1/abs(float(x))))

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












from math import cos,sin,tan,radians,sqrt




def circle_intersection(circle1, circle2):
    x1,y1,r1 = circle1
    x2,y2,r2 = circle2
    # http://stackoverflow.com/a/3349134/798588
    dx,dy = x2-x1,y2-y1
    d = sqrt(dx*dx+dy*dy)
    if d > r1+r2:
        #print ("#1")
        return False # no solutions, the circles are separate
    if d < abs(r1-r2):
        #print ("#2")
        return False # no solutions because one circle is contained within the other
    if d == 0 and r1 == r2:
        #print ("#3")
        return False # circles are coincident and there are an infinite number of solutions

    a = (r1*r1-r2*r2+d*d)/(2*d)
    h = sqrt(r1*r1-a*a)
    xm = x1 + a*dx/d
    ym = y1 + a*dy/d
    xs1 = xm + h*dy/d
    xs2 = xm - h*dy/d
    ys1 = ym - h*dx/d
    ys2 = ym + h*dx/d

    xs1=round(xs1)
    ys1=round(ys1)

    xs2=round(xs2)
    ys2=round(ys2)
    return (xs1,ys1),(xs2,ys2)


def point_make(lenth):
    simple_angle=radians(30)
    point1_x=0.5*lenth*-1
    point1_y=-0.5*lenth*tan(simple_angle)
    #print("point1",point1_x,point1_y)

    point2_x=0.5*lenth
    point2_y=-0.5*lenth*tan(simple_angle)
    #print("point2",point2_x,point2_y)

    point3_x=0
    point3_y=point2_y**2+(0.5*lenth)**2
    point3_y=point3_y**0.5
    #print("point3",point3_x,point3_y)

    return((point1_x,point1_y),(point2_x,point2_y),(point3_x,point3_y))













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


teast_loop=0
while 1:
    print("teast_loop",teast_loop)
    teast_loop=teast_loop+1
    #print("list of all thered runing data")
    a,b,c=thead_list
    #time.sleep(0.5)



    #dicethan sedon apart
    temp=point_make(5)
    A=temp[0][0],temp[0][1],a.therd_data
    B=temp[1][0],temp[1][1],b.therd_data
    C=temp[2][0],temp[2][1],c.therd_data

    print("size of circels",A[2],B[2],C[2])
    if teast_loop>6:
        print("STOP")
        for q in thead_list:
            q.mark=False

        exit()
    count=0

    point_match=[]

    #print("test start")
    #print(circle_intersection(point2,point3))
    #print("etast end")

    inersection_point=[]




    inersection_point.append(circle_intersection(A,B))
    inersection_point.append(circle_intersection(A,C))
    inersection_point.append(circle_intersection(B,C))

    print("intersection points",inersection_point)


    for q in inersection_point:

        for w in q:
            #print("w",w)
            #print("q",q)
            marker=True
            for t in inersection_point:
                #print("t",t)
                #print("w",w)
                if not (w in t):
            #        print("W no in t ")
                    marker=False
            #    if q==t:
            #        print("comparing same point")
                    #marker=False
                #print("q",q)
                #print("w",w)
                #print("T",t)
                #print("")
            if marker==True:
                print("point found",w)













print ("Exiting Main Thread")
exit()
