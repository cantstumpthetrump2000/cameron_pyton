from PIL import Image
import numpy


im = Image.open("teast2.png")


#vaule coulers_found['237-28-36', '255-255-255', '34-177-76']
coulers_found=set()
pix = numpy.array(im)

for y in pix:
    for x in y:
        red,green,blue=x
        temp=str(red)+"-"+str(green)+"-"+str(blue)
        coulers_found.add(temp)


print("no red box ")
print("coulers_found",coulers_found)
