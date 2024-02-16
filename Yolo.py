from typing import List, Dict
import torch
import numpy as np

class Yolo():

    def __init__(self, model_path, weight_path):
        self.model_path = model_path
        self.weight_path = weight_path
        self.device = None
        self.model = None

        #  Initialisation du modèle, en vérifiant si CUDA est disponible ou non, et en stockage avec torch.hub.load sur une version locale de Yolov5

    def build(self):

        # Si CUDA est disponible, utiliser le GPU, sinon utiliser le CPU
        if torch.cuda.is_available():
            self.device = torch.device('cuda')
        else:
            self.device = torch.device('cpu')

        # Initialisation du modèle
        self.model = torch.hub.load(repo_or_dir=self.model_path, device=self.device, model="custom", source="local",
                                    path=self.weight_path, force_reload=True)

        # Déplacement du modèle vers le périphérique disponible
        self.model = self.model.to(self.device)

        # Prend en entrée une image et renvoie la liste des prédictions avec leurs coordonnées

    def predict(self, frames: List[np.ndarray]) -> List[Dict[str, List]]:

        result: List = []

        inference = self.model(frames)

        for i, detection in enumerate(inference.pandas().xyxy):
            for row in detection.itertuples():
                result.append(row)
        return result


