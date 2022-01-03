
import cv2
from matplotlib import pyplot as plt
#Chargement de l'image en niveau de gris
img = cv2.imread(r'lisa.png')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

"""
Il y a beaucoup de sombre dans l'image puis un dégradé de couleurs plus claires mais pas de blanc total
"""
plt.subplot(1,3,3)
plt.hist(imgGray.ravel(),256,[0,256]) 
plt.subplot(1,3,2)
plt.imshow(imgGray,cmap = 'gray')
plt.title('Gris'), plt.xticks([]), plt.yticks([])
plt.subplot(1,3,1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB),cmap = 'autumn')
plt.title('Originale'), plt.xticks([]), plt.yticks([])

plt.show()