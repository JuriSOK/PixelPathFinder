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
    """
    La fonction permet de convertir une matrice numpy (d'une image en niveau de gris) en un graphe valué.
    Chaque pixel est un sommet du graphe, et les arêtes représentent la différence d'intensité entre deux pixels adjacents.
    
    :param image_array: Une matrice numpy représentant l'image en niveaux de gris.
    :return: Un graphe représentant l'image
    """
    nb_lignes = image_array.shape[0]
    nb_colonnes = image_array.shape[1]

    graphe = Graphe()

    # Ajout des sommets (ce sont les pixels de l'image)
    for i in range (nb_lignes):
        for j in range (nb_colonnes):
            indivTime = image_array[i,j]
            graphe.ajouter_sommet(indivTime)


    # Ajout des arêtes (ce sont les différences d'intensités entre deux arêtes voisines)
    for i in range (nb_lignes):
        for j in range (nb_colonnes):

            source = i * nb_colonnes + j

            #Voisin en haut
            if i>0:
                dest = (i - 1) * nb_colonnes + j
                poids = abs(image_array[i-1, j] - image_array[i, j]) 
                graphe.ajouter_arete(source, dest, poids)
                

            #Voisin à gauche
            if (j>0):
                dest = i * nb_colonnes + (j-1)
                poids = abs(image_array[i, j-1] - image_array[i, j])
                graphe.ajouter_arete(source, dest, poids)
                  

            #Voisin en bas
            if i < (nb_lignes -1):
                dest = (i+1) * nb_colonnes + j
                poids = abs(image_array[i+1, j] - image_array[i, j])
                graphe.ajouter_arete(source, dest, poids)

            
            #Voisin à droite

            if j < (nb_colonnes -1):
                dest = i * nb_colonnes + (j+1)
                poids = abs(image_array[i, j+1] - image_array[i, j])
                graphe.ajouter_arete(source, dest, poids)


    return graphe





               



            




           


