import time
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox
from img_manager import image_to_graphe, load_image



class PixelPathFinderApp:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = Image.open(image_path)
        self.largeur, self.hauteur = self.image.size
        self.pixels, self.graphe = self.prepare_graphe()

        self.sommet_depart = None
        self.sommet_arrivee = None

        self.root = tk.Tk()
        self.root.title("PixelPathFinder - Mini Projet Algo L3")

        self.canvas = tk.Canvas(self.root, width=self.largeur, height=self.hauteur)
        self.canvas.pack()

        # Affichage de l'image en arrière-plan
        self.photo = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)


        self.canvas.bind("<Button-1>", self.on_click)

        self.root.mainloop()

    def prepare_graphe(self):
        print("Conversion de l'image en graphe...")
        pixels, largeur, hauteur = load_image(self.image_path)
        graphe = image_to_graphe(pixels, largeur, hauteur)
        return pixels, graphe


    def on_click(self, event):
        x, y = event.x, event.y
        sommet = y * self.largeur + x

        if self.sommet_depart is None:
            self.sommet_depart = sommet
            self.highlight_pixel(x, y, "green")
            print(f"Point de départ sélectionné : ({x}, {y})")
        elif self.sommet_arrivee is None:
            self.sommet_arrivee = sommet
            self.highlight_pixel(x, y, "red")
            print(f"Point d'arrivée sélectionné : ({x}, {y})")
            self.calculate_and_draw_path()
        else:
            messagebox.showinfo("Réinitialiser", "Déjà deux points sélectionnés. Relancez l'application pour réessayer.")

    def highlight_pixel(self, x, y, color):
        self.canvas.create_rectangle(
            x - 3, y - 3, x + 3, y + 3, fill=color, outline=color
        )

    def calculate_and_draw_path(self):
        start_time = time.time()  # Temps avant le calcul du chemin
        print("Calcul du plus court chemin avec Dijkstra...")

        chemin = self.graphe.dijkstra(self.sommet_depart, self.sommet_arrivee)

        for sommet in chemin:
            x = sommet % self.largeur
            y = sommet // self.largeur
            self.canvas.create_oval(
                x - 1, y - 1, x + 1, y + 1, fill="blue", outline="blue"
            )

        end_time = time.time()  # Temps après le calcul du chemin
        elapsed_time = end_time - start_time  # Temps écoulé
        print(f"Calcul terminé en {elapsed_time:.4f} secondes.")  # Affichage du temps dans la console