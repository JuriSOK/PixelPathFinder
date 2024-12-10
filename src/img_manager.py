from PIL import Image
from graph import Graphe

def load_image(image_path):
    """
    La fonction permet de charger une image depuis le chemin spécifié et de renvoyer ces informations :
    liste de pixels, largeur, hauteur.
    :param image_path: Le chemin de l'image
    :return: Une liste de pixels représentant l'image en niveaux de gris, sa largeur et sa hauteur
    """
    image = Image.open(image_path).convert('L')  # Conversion en niveaux de gris
    pixels = image.load()  # Charge les pixels de l'image
    largeur, hauteur = image.size 
    return pixels, largeur, hauteur


def image_to_graphe(pixels, largeur, hauteur):
    """
    La fonction permet de convertir une image en graphe valué.
    Chaque pixel est un sommet du graphe, et les arêtes représentent la différence d'intensité entre deux pixels adjacents.
    
    :param pixels: La liste des pixels de l'image
    :param largeur: La largeur de l'image
    :param hauteur: La hauteur de l'image
    :return: L'image transformée en graphe.
    """
    graphe = Graphe()

    # Ajout des sommets (ce sont les pixels de l'image)
    # on fait un for y puis un for x car le format d'un pixel est [colonne,ligne].
    for y in range(hauteur): 
        for x in range(largeur):
            indivTime = pixels[x, y]  
            graphe.ajouter_sommet(indivTime)

    # Ajout des arêtes (ce sont les différences d'intensités entre deux sommets voisins)
    for y in range(hauteur):
        for x in range(largeur):

            source = y * largeur + x  # Calculer l'indice du sommet actuel

            # Voisin en haut
            if y > 0:
                dest = (y - 1) * largeur + x
                poids = abs(pixels[x, y - 1] - pixels[x, y])
                graphe.ajouter_arete(source, dest, poids)

            # Voisin à gauche
            if x > 0:
                dest = y * largeur + (x - 1)
                poids = abs(pixels[x - 1, y] - pixels[x, y])
                graphe.ajouter_arete(source, dest, poids)

            # Voisin en bas
            if y < hauteur - 1:
                dest = (y + 1) * largeur + x
                poids = abs(pixels[x, y + 1] - pixels[x, y])
                graphe.ajouter_arete(source, dest, poids)

            # Voisin à droite
            if x < largeur - 1:
                dest = y * largeur + (x + 1)
                poids = abs(pixels[x + 1, y] - pixels[x, y])
                graphe.ajouter_arete(source, dest, poids)

    return graphe





           


