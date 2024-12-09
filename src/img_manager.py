import numpy as np
from PIL import Image
from graph import Graphe

def load_image(image_path):
    """
    La fonction permet de charger une image depuis le chemin spécifié puis la convertit en niveaux de gris.
    :param image_path: Le chemin de l'image
    :return: Une matrice numpy représentant l'image en niveaux de gris
    """
    image = Image.open(image_path).convert('L')  # Conversion en niveaux de gris
    image_array = np.array(image)
    return image_array


def image_to_graphe(image_array):

    graphe = Graphe()

    # Ajout des sommets (ce sont les pixels de l'image)
    for i in range (image_array.shape[0]):
        for j in range (image_array.shape[1]):
            indivTime = image_array[i,j]
            graphe.ajouter_sommet(indivTime)



    # Ajout des arêtes (ce sont les différences d'intensités entre deux arêtes voisines)

    for i in range (image_array[0]):
        for j in range (image_array[1]):

            source = i * image_array.shape[1] + j

            




           


