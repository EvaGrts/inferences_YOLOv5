import cv2
import numpy as np


# Ecrit du texte, directement sur l'image qu'on lui donne en entrée
def text(image, text, position, font, font_scale, color, thickness):
    # Ajout du texte sur l'image 
    cv2.putText(image, text, position, font, font_scale, color, thickness)

    # Renvoi de l'image modifiée 
    return image


# Dessine un rectangle, directement sur l'image qu'on lui donne en entrée
def bbox(image, top_left, bottom_right, color, thickness):

    # Dessin de rectangle 
    cv2.rectangle(image, top_left, bottom_right, color, thickness)

    # Renvoi de l'image modifiée
    return image


# Prend en entrée une image et une liste de prédictions, et renvoie l'image annotée avec les bounding boxes, le nom de la classe et le pourcentage de précision
def annotate_frame(image, lst_pred):
    annotated_image = np.copy(image)

    for detection_group in lst_pred:
        top_left = (int(detection_group.xmin), int(detection_group.ymin))
        bottom_right = (int(detection_group.xmax), int(detection_group.ymax))
        class_name = detection_group.name
        confidence = detection_group.confidence

        # Dessin de la bounding box sur l'image
        bbox(annotated_image, top_left, bottom_right, color=(0, 255, 0), thickness=2)

        # Création du texte d'annotation
        label = f"{class_name}: {confidence:.2%}"

        # Affichage du texte à côté de la bounding box
        text_position = (top_left[0], top_left[1] - 10)
        text(annotated_image, label, text_position, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    return annotated_image


# Prend en entrée une image et l'affiche avec OpenCV
def display_frame(image):
    # Affichage de l'image dans une fenêtre avec le titre "Image"
    cv2.imshow('Image', image)

    cv2.waitKey(1)