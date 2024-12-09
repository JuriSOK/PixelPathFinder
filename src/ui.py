# ui.py
import tkinter as tk
from PIL import Image, ImageTk, ImageDraw
import numpy as np
from img_manager import image_to_graphe  # Importer la fonction qui convertit l'image en graphe

class PixelPathFinderApp:
    def __init__(self, root, image_path):
        self.root = root
        self.image_path = image_path  # Sauvegarder le chemin de l'image
        self.root.title("Pixel Path Finder")
        
        # Charger l'image directement à partir du chemin
        self.image = Image.open(image_path).convert("RGB")
        self.image_array = np.array(self.image.convert('L'))  # Convertir l'image en niveaux de gris
        self.graphe = image_to_graphe(self.image_array)  # Convertir l'image en graphe
        
        self.canvas = tk.Canvas(self.root, width=500, height=500)
        self.canvas.pack()

        self.start_pixel = None
        self.end_pixel = None
        
        self.display_image()

    def display_image(self):
        # Afficher l'image dans le canevas
        self.image_tk = ImageTk.PhotoImage(self.image.resize((500, 500)))
        self.canvas.create_image(0, 0, anchor="nw", image=self.image_tk)
        self.canvas.bind("<Button-1>", self.select_pixel)

    def select_pixel(self, event):
        # Sélectionner un pixel (soit départ, soit arrivée)
        if self.start_pixel is None:
            self.start_pixel = (event.y * self.image_array.shape[0] // 500, event.x * self.image_array.shape[1] // 500)
            print(f"Pixel de départ: {self.start_pixel}")
        elif self.end_pixel is None:
            self.end_pixel = (event.y * self.image_array.shape[0] // 500, event.x * self.image_array.shape[1] // 500)
            print(f"Pixel d'arrivée: {self.end_pixel}")
            self.highlight_path()

    def calculate_path(self):
        if self.start_pixel and self.end_pixel:
            start_idx = self.start_pixel[0] * self.image_array.shape[1] + self.start_pixel[1]
            end_idx = self.end_pixel[0] * self.image_array.shape[1] + self.end_pixel[1]
            # Calculer le plus court chemin avec Dijkstra
            chemin = self.graphe.dijkstra(start_idx, end_idx)
            self.highlight_path(chemin)

    def highlight_path(self, chemin=None):
        if chemin is None:
            return
        # Créer une nouvelle image pour dessiner le chemin
        path_image = self.image.copy()
        draw = ImageDraw.Draw(path_image)
        
        # Surligner le chemin en bleu
        for idx in chemin:
            i, j = divmod(idx, self.image_array.shape[1])  # Conversion de l'index en coordonnées (i, j)
            draw.point((j * 500 // self.image_array.shape[1], i * 500 // self.image_array.shape[0]), fill="blue")
        
        # Surligner les sommets en rouge
        for idx in range(len(self.graphe.liste_sommet)):
            i, j = divmod(idx, self.image_array.shape[1])
            draw.point((j * 500 // self.image_array.shape[1], i * 500 // self.image_array.shape[0]), fill="red")
        
        self.image_tk = ImageTk.PhotoImage(path_image.resize((500, 500)))
        self.canvas.create_image(0, 0, anchor="nw", image=self.image_tk)
        self.canvas.update()
