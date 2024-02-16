import threading
import atexit 


class Camera(threading.Thread): 
    
    def __init__(self, video):
        super(Camera, self).__init__() 
        self.video = video
        self.latest_image = None 
        # Enregistrement de la fonction clean pour qu'elle soit appelée à la fin du programme
        atexit.register(self.clean) 


    # Stocke l'image la plus récente du flux vidéo
    def run(self):
        # On boucle à l'infinie 
        while True:
            # On prend une photo 
            ret, image = self.video.read()  # ret : booléen pour savoir si l'image est bien prise | image : image prise 
            if ret:
                self.latest_image = image 


    # Récupère l'image la plus récente stockée, depuis l'extérieur de la classe
    def read(self): 
        # Renvoie de l'image prise 
        return self.latest_image  


    # Nettoye les flux vidéos et libérer les caméras à la fin de programme et/ou en cas de crash 
    def clean(self): 
        if self.video.isOpened():
            self.video.release()



    