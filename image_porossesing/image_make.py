from PIL import Image
import numpy


im = Image.open("teast2.png")

print("image info",im.format, im.size, im.mode)

#vaule coulers_found['237-28-36', '255-255-255', '34-177-76']
coulers_found=set()
pix = numpy.array(im)
count=0





y_postion=-1
for y in pix:
    y_postion+=1
    x_postion=-1
    for x in y:
        x_postion+=1
        red,green,blue=x
        temp=str(red)+"-"+str(green)+"-"+str(blue)
        coulers_found.add(temp)
        if red<255 and green<255 and blue<255:
            count+=1
            pix[y_postion][x_postion]=(0,0,0)






iamge2=Image.fromarray(pix)
iamge2.show()
iamge2.save("hello.png")







print(count)
print("coulers_found",coulers_found)
