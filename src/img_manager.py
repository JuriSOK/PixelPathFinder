import numpy as np
from PIL import Image

def load_image(image_path):
    """
    La fonction permet de charger une image depuis le chemin spécifié puis la convertit en niveaux de gris.
    :param image_path: Le chemin de l'image
    :return: Une matrice numpy représentant l'image en niveaux de gris
    """
    image = Image.open(image_path).convert('L')  # Conversion en niveaux de gris
    image_array = np.array(image)
    return image_array