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
imgZebre = cv2.imread(r'.\zebre.jpg')
imgZebre = cv2.cvtColor(imgZebre, cv2.COLOR_BGR2GRAY)
imgSuzan = cv2.imread(r'.\suzan.jpg')
imgSuzan = cv2.cvtColor(imgSuzan, cv2.COLOR_BGR2GRAY)

#Applique une transformation pour détecter la profondeur 
sobelx = cv2.Sobel(imgZebre,cv2.CV_64F,0,1,ksize=5)
sobely = cv2.Sobel(imgSuzan,cv2.CV_64F,1,0,ksize=5)


#Affiche les images transformées ainsi que l'originale
plt.subplot(2,2,1),plt.imshow(imgZebre,cmap = 'gray')
plt.title('original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(imgSuzan,cmap = 'gray')
plt.title('original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.show()