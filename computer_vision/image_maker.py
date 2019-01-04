from PIL import Image
import numpy as np
from random import randint



# write array to img
def create_img(width, height):
    rgb_array = np.zeros((width, height, 3), 'uint8')
    for x in range(0, width):
        for y in range(0, height):
            rgb_array[x, y, 0] = randint(0, 255) #R
            rgb_array[x, y, 1] = randint(0, 255) #G
            rgb_array[x, y, 2] = randint(0, 255) #B

    img = Image.fromarray(rgb_array)
    img.save('img.jpeg')


# write bin_array to img
create_img(640, 640)
