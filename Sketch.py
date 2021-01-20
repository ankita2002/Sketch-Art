import cv2
import imageio
import numpy as np
import scipy.ndimage

img = "ankita.jpg"

def grayscale(rgb):
    return np.dot(rgb[...,:3],[0.299,0.587,0.114])

def dodge(front,back):
    result = front*255/(255-back)
    result[result>255]=255
    result[back==255]=255
    return result.astype('uint8')

s = imageio.imread(img)
g = grayscale(s)
i = 190-g

b = scipy.ndimage.filters.gaussian_filter1d(i,sigma=50)
r = dodge(b,g)

cv2.imwrite('An2.png',r)
print("Task Complete.....")
