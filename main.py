import cv2 
from Camera import Camera
from Yolo import Yolo
from app import app

def main():

    # Initialisation de la caméra
    video_capture = cv2.VideoCapture(0)
    camera = Camera(video_capture)
    camera.start() 

    yolo_model_path = 'yolov5/yolov5-master'
    yolo_weight_path = 'yolov5s.pt' 

    # Initialisation de YOLO
    yolo = Yolo(yolo_model_path, yolo_weight_path)
    yolo.build()

    # Lancement de l'application
    app(camera, yolo)


main()