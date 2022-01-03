# Mon script OpenCV : Video_processing
#
import numpy as np
import cv2

#Modifie une image de la vidéo
def frame_processing(imgc):
    laplacian = cv2.Laplacian(imgc,cv2.CV_64F)

    #Applique une transformation pour détecter la profondeur 
    sobelx = cv2.Sobel(imgc,cv2.CV_64F,1,0,ksize=5)
    sobely = cv2.Sobel(imgc,cv2.CV_64F,0,1,ksize=5)

    canny = cv2.Canny(imgc,30,150)
    return imgc, laplacian, sobelx, sobely, canny

#Charge la vidéo
cap = cv2.VideoCapture('jurassicworld.mp4')

#Tant que la vidéo n'est pas finie
while (True):

    #Récupération d'une frame de la vidéo
    ret, frame = cap.read()

    #Si la vidéo n'est pas finie
    if ret == True:
        #Copie de l'image en niveau de gris
        img = frame.copy()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        #Applique une transformation sur l'image en niveau de gris
        gray, laplacian, sobelx, sobely, canny = frame_processing(gray)



        #Affiche l'image en niveau de gris transformée et l'image originale
        cv2.imshow('MavideoAvant', frame)
        cv2.imshow('MavideoApres', gray)
        cv2.imshow('laplacien', laplacian)
        cv2.imshow('sobelX', sobelx)
        cv2.imshow('sobelY', sobely)
        cv2.imshow('canny', canny)



    else:
        print('video ended')
        break

    if cv2.waitKey(int(1/30*1000)) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows() 

"""Q5
Perte d'informations
Paramètres non changeants et à définir à la main
Prise en compte locale uniquement sans prendre en compte l'image complète
"""