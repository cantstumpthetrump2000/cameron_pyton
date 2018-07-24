from PIL import Image
import numpy
import time
start=time.time()
im = Image.open("hello.png")


#vaule coulers_found['237-28-36', '255-255-255', '34-177-76']


coulers_found={}
array_to_use = numpy.array(im)

loopcounter=0

scan=[[1,0],[-1,0],[0,1],[0,-1]]

look_for_vaule=(0,0,0)

x_postion=-1
y_postion=-1

box=[]
qwe=0

point_to_look_at=[]


for y in array_to_use:
    y_postion=y_postion+1

    x_postion=-1

    for x in y:
        x_postion=x_postion+1


        if (x ==look_for_vaule).all():
            current_potion=((y_postion,x_postion))
            allready_coved=False
            for q in box:
                if current_potion in q:
                    allready_coved=True
            if allready_coved==False:
                box.append([])

                box[len(box)-1].append(current_potion)

                print("starting point",current_potion)

                while 1:

                    for q in scan:
					#	qwe=qwe+1
                        #print("#############")
                        #print("point posstrion",(current_potion[0]+q[0],current_potion[1]+q[1]))
                        #print ("point vaule",array_to_use[current_potion[0]+q[0]][current_potion[1]+q[1]])

                        VAULE_MATCH=False
                        if (array_to_use[current_potion[0]+q[0]][current_potion[1]+q[1]] ==look_for_vaule).all():
                            VAULE_MATCH=True
                        #print("VAULE_MATCH",VAULE_MATCH)

                        got_already=False
                        if (current_potion[0]+q[0],current_potion[1]+q[1]) in box[len(box)-1]:
                            got_already=True
                        #print("got_already",got_already)




                        #print("#############")



                        if VAULE_MATCH==True and got_already==False   :
                            #print("new point to look at ",(current_potion[0]+q[0],current_potion[1]+q[1]))
                            point_to_look_at.append((current_potion[0]+q[0],current_potion[1]+q[1]))
                            box[len(box)-1].append((current_potion[0]+q[0],current_potion[1]+q[1]))
                    #print(box[len(box)-1])

                    if len(point_to_look_at)==0:
                        break
                    current_potion=point_to_look_at[0]
                    #print("new cuuren",current_potion)

                    point_to_look_at.remove(current_potion)
                    #print()





print("number of boxes found",len(box))
end=time.time()
print("total time",end-start)
#print("number of loops",loop_counter)
