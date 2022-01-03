# Image Processing with OpenCV

import cv2
import os
import sys
import numpy as np
from matplotlib import pyplot as plt


#Affichage des versions de python et opencv
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)

print("OPENCV Version =", cv2.__version__)

rep_cour = os.getcwd()
print(rep_cour)

#Chargement de l'image en niveau de gris
img = cv2.imread(r'.\boats.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

(thresh, imgBinary) = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

#Affiche les images transformées ainsi que l'originale
cv2.imshow("Originale",img)
cv2.imshow("Binaire",imgBinary)

cv2.waitKey()
