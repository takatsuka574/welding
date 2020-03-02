import cv2
import numpy as np

def to_polar(image,s0,s1,value):
     polar_image = cv2.linearPolar(image,(s1, s0), value, cv2.WARP_FILL_OUTLIERS)
     polar_image=cv2.resize(polar_image, (500, 200), interpolation = cv2.INTER_AREA)
     return polar_image
1
