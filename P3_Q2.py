import cv2

# On charge les images
image1 = cv2.imread("jeu1.jpg")
image2 = cv2.imread("jeu2.jpg")

# On soustrait les images l'une par rapport à l'autre pour obtenir toutes les différences
difference = cv2.subtract(image1, image2)
difference2 =  cv2.subtract(image2, image1)


# On colore les différences (rouge pour difference, vert pour difference2) pour les remarquer plus facilement
Conv_hsv_Gray = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(Conv_hsv_Gray, 0, 255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
Conv_hsv_Gray2 = cv2.cvtColor(difference2, cv2.COLOR_BGR2GRAY)
ret2, mask2 = cv2.threshold(Conv_hsv_Gray2, 0, 255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
difference[mask != 255] = [0, 0, 255]
difference2[mask2 != 255] = [0, 255, 0]

#Permet de voir les différences sur les images originales directement (optionnel)
image1[mask != 255] = [0, 0, 255]
image2[mask2 != 255] = [0, 255, 0]

#On fusionne nos deux images de différences obtenues par soustraction pour voir toutes les différences sur une unique image
differenceTotal = cv2.addWeighted(difference,0.5,difference2,0.5,0)

#On affiche les différentes images obtenues
cv2.imshow('image1',image1)
cv2.imshow('image2',image2)
#cv2.imshow('differenceRouge',difference)
#cv2.imshow('differenceRouge2',difference2)
cv2.imshow('differenceTotal',differenceTotal)
cv2.waitKey()