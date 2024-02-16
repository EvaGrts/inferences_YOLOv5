from display import annotate_frame, display_frame

def app(camera, yolo):
    # Lancement de la boucle infinie
    while True:
        # Récupération de l'image depuis la caméra
        image = camera.read()

        # Vérification si une image est disponible
        if image is not None:
            # Prédiction avec YOLO
            predictions = yolo.predict(image)

            # Annotation de l'image avec les prédictions
            annotated_image = annotate_frame(image, predictions)

            # Affichage de l'image annotée
            display_frame(annotated_image)