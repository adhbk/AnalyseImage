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

#Applique une transformation pour détecter les contours (passe-haut)
laplacian = cv2.Laplacian(img,cv2.CV_64F)

#Applique une transformation pour détecter la profondeur 
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

#Affiche les images transformées ainsi que l'originale
plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
plt.show()