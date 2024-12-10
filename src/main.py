from img_manager import load_image, image_to_graphe
from ui import afficher_chemin
from tkinter import messagebox
import time

def main():

    # Afficher le pop-up avant de commencer le calcul
    messagebox.showinfo("Calcul du chemin", "Chemin en cours de recherche...")

    image_path = "/Users/arnaudsok/Documents/L3/Algo_A/PixelPathFinder/res/Mona_LisaBlackWhite.png"  # Remplace par le chemin réel
    print("Chargement de l'image...")
    pixels, largeur, hauteur = load_image(image_path)

    print("Conversion de l'image en graphe...")
    graphe = image_to_graphe(pixels, largeur, hauteur)

    # Points de départ et d'arrivée pour Dijkstra
    sommet_depart = 0  # Premier pixel (en haut à gauche)
    #sommet_arrivee = (hauteur * largeur) - 1 # Dernier pixel (en bas à droite)
    sommet_arrivee = 2300
    print("Calcul du plus court chemin avec Dijkstra...")
    chemin = graphe.dijkstra(sommet_depart, sommet_arrivee)

    # Simuler un délai pour montrer le pop-up pendant le calcul
    time.sleep(2)  # Simule le temps de calcul du chemin (retirer pour la version finale)


    print("Affichage du chemin...")
    afficher_chemin(image_path, chemin, sommet_depart, sommet_arrivee, largeur, hauteur)

    

if __name__ == "__main__":
    main()