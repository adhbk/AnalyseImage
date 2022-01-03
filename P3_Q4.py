import cv2
import numpy as np
# On charge les images
image = cv2.imread("cellules.png")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
oui = np.array([])
print(f"{cv2.connectedComponents(image,labels=image,connectivity=4,ltype=cv2.CV_32S)[0]} éléments")
cv2.imshow('avant',image)
cv2.fastNlMeansDenoising(image,dst=image,h=33)
print(f"{cv2.connectedComponents(image,labels=image,connectivity=4,ltype=cv2.CV_32S)[0]} éléments")

cv2.imshow('',image)


cv2.waitKey()