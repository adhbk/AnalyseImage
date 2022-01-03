from scipy import ndimage
import cv2
import math
#rotation angle in degree

image = cv2.imread("lena.jpg")



import numpy as np
import cv2
"""
def rotate(image, angle):
  image_center = tuple(np.array(image.shape[1::-1]) / 2)
  rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
  result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
  return result
"""
def rotate(image, angle):
    row,col,a = np.array(image).shape
    center=tuple(np.array([row,col])/2)
    rot_mat = cv2.getRotationMatrix2D(center,angle,1.0)
    new_image = cv2.warpAffine(image, rot_mat, (col,row))
    return new_image

rotated = rotate(image, 45)
rotated = rotate(rotated, 45)
rotated = rotate(rotated, 45)
rotated = rotate(rotated, 45)
rotated = rotate(rotated, 45)
rotated = rotate(rotated, 45)
rotated = rotate(rotated, 45)
rotated = rotate(rotated, 45)

cv2.imwrite("lena_rotated.jpg",rotated)
