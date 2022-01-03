
import cv2
from matplotlib import pyplot as plt
#Chargement de l'image en niveau de gris
img = cv2.imread(r'paysage.jpg')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgGrayEq = cv2.equalizeHist(imgGray)
"""
Il y a beaucoup de sombre dans l'image puis un dégradé de couleurs plus claires mais pas de blanc total
"""

plt.subplot(2,3,1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Originale'), plt.xticks([]), plt.yticks([])

plt.subplot(2,3,2)
plt.imshow(imgGray,cmap = 'gray')
plt.title('Gris'), plt.xticks([]), plt.yticks([])

plt.subplot(2,3,3)
plt.imshow(imgGrayEq,cmap = 'gray')
plt.title('Gris Egalisé'), plt.xticks([]), plt.yticks([])

plt.subplot(2,3,5)
plt.hist(imgGray.ravel(),256,[0,256]) 

plt.subplot(2,3,6)
plt.hist(imgGrayEq.ravel(),256,[0,256]) 

plt.show()

#Chargement de l'image en niveau de gris
img2 = cv2.imread(r'soleil.png')
imgGray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
imgGrayEq2 = cv2.equalizeHist(imgGray2)
"""
Il y a beaucoup de sombre dans l'image puis un dégradé de couleurs plus claires mais pas de blanc total
"""
plt.subplot(2,3,1)
plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
plt.title('Originale'), plt.xticks([]), plt.yticks([])

plt.subplot(2,3,2)
plt.imshow(imgGray2,cmap = 'gray')
plt.title('Gris'), plt.xticks([]), plt.yticks([])

plt.subplot(2,3,3)
plt.imshow(imgGrayEq2,cmap = 'gray')
plt.title('Gris Egalisé'), plt.xticks([]), plt.yticks([])

plt.subplot(2,3,5)
plt.hist(imgGray2.ravel(),256,[0,256]) 

plt.subplot(2,3,6)
plt.hist(imgGrayEq2.ravel(),256,[0,256]) 

plt.show()