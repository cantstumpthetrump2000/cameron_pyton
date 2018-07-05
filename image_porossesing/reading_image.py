from PIL import Image
import numpy


im = Image.open("teast_image_1.png")

print("image info",im.format, im.size, im.mode)


pix = numpy.array(im)

print("pix 0,0",pix[0][0])
