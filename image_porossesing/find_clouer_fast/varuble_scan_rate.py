
#incomeing image rate  1 image every 0.0333333333333333 second from kinect caram

from PIL import Image
import numpy
import time

im = Image.open("image1.png")


#vaule coulers_found['237-28-36', '255-255-255', '34-177-76']
pix = numpy.array(im)
size_of_image_y=len(pix)
size_of_image_x=len(pix[0])

total_number_of_pixes=size_of_image_x*size_of_image_y

print("image size is ")
print("y size ",size_of_image_y)
print("x size ",size_of_image_x)


def sacn_function(step_to_take=1,teast=False):
    #coulers_found = set()
    coulers_found={}
    start=time.time()

    #step_to_take=10

    for y in range(0,size_of_image_y,step_to_take):
        for x in range(0,size_of_image_x,step_to_take):
            cureent_vaule=pix[y][x]
            red,green,blue=cureent_vaule
            temp=str(red)+"-"+str(green)+"-"+str(blue)
            if temp in coulers_found.keys():
                coulers_found[temp].append((y,x))
            else:
                coulers_found[temp]=[[y,x]]
            #coulers_found.add(temp)



    end=time.time()
    total_time=end-start
    if teast==True:
        print("time it took",total_time)

        print("coulers_found",)

        for q in coulers_found:
            print(q)
    return (coulers_found)
def tesat():
    for q in range(1,100):
        tep=sacn_function(q,True)
        #print(tep)
        print("step rate")
        print(q)
        if len(tep.keys())<5:
            print("missed a couler")
            break


coouler_found=sacn_function()
for q in coouler_found:

    cuales=coouler_found[q]
    max_f=0,[0,0]
    min_f=total_number_of_pixes,[0,0]
    for w in cuales:
        y,x=w
        scoere=y+x
        #print("score",scoere)
        if scoere>max_f[0]:
            max_f=scoere,[y,x]
        if scoere<min_f[0]:

            min_f=scoere,[y,x]
    print("min point for ", q, " is ", min_f[1])
    print("max point for ",q ," is ",max_f[1])
    x_size=max_f[1][1]-min_f[1][1]
    y_size=max_f[1][0]-min_f[1][0]


    mindel_point=min_f[1][0]+y_size/2,min_f[1][1]+x_size/2
    mindel_point=round(mindel_point[0]),round(mindel_point[1])
    size_of_couler=y_size*x_size
    print("size of the couler is ",size_of_couler)
    print("the midel point is ",mindel_point)
    print("")