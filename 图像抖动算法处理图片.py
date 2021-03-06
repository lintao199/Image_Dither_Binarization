
import numpy as np
from PIL import Image
image_file = 'C:\\Users\\lin\\Desktop\\photo12.jpg'
img=Image.open(image_file)


img_width,img_height=img.size
bayer=np.array([[0, 48, 12, 60, 3, 51, 15, 63],
                [32, 16, 44, 28, 35, 19, 47, 31],
                [8, 56, 4, 52, 11, 59, 7, 55],
                [40, 24, 36, 20, 43, 27, 39, 23],
                [2, 50, 14, 62, 1, 49, 13, 61],
                [34, 18, 46, 30, 33, 17, 45, 29],
                [10, 58, 6, 54, 9, 57, 5, 53],
                [42, 26, 38, 22, 41, 25, 37, 21]])



for i in range(img_height):
    for j in range(img_width):
        s=img.getpixel((j,i))
        a=sum(s)/12
        if(a<bayer[i%7][j&7]):
            img.putpixel((j,i),0)
        else:
            img.putpixel((j,i),(255,255,255))
            
img.show()


