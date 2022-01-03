# Mon script OpenCV : Video_processing
#
import numpy as np
import cv2

#Modifie une image de la vidéo
def frame_processing(imgc):
     return imgc

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
        gray = frame_processing(gray)

        #Affiche l'image en niveau de gris transformée et l'image originale
        cv2.imshow('MavideoAvant', frame)
        cv2.imshow('MavideoApres', gray)

    else:
        print('video ended')
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows() 