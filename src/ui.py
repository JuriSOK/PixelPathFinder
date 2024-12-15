import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import time

from img_manager import load_image, image_to_graphe
from graph import Graphe

class PixelPathFinderApp:
    def __init__(self):
        self.image_path = None
        self.image = None
        self.largeur, self.hauteur = None, None
        self.pixels = None
        self.graphe = None

        self.sommet_depart = None
        self.sommet_arrivee = None

        self.root = tk.Tk()
        self.root.title("PixelPathFinder - Mini Projet Algo L3")

        # Cadre principal
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Canvas pour l'image
        self.canvas_frame = tk.Frame(self.main_frame)
        self.canvas_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.canvas = tk.Canvas(self.canvas_frame, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Menu à droite
        self.menu_frame = tk.Frame(self.main_frame, width=300, bg="lightgray")
        self.menu_frame.pack(side=tk.RIGHT, fill=tk.Y)

        self.create_menu()
        self.root.mainloop()

    def create_menu(self):
        """Crée les widgets pour le menu à droite."""
        # Champ pour le chemin de l'image
        tk.Label(self.menu_frame, text="Chemin de l'image:", bg="lightgray").pack(pady=10)
        self.image_path_entry = tk.Entry(self.menu_frame, width=30)
        self.image_path_entry.pack(pady=5)
        tk.Button(self.menu_frame, text="Charger l'image", command=self.load_image).pack(pady=5)

        self.image_dimensions_label = tk.Label(self.menu_frame, text="Dimensions: N/A", bg="lightgray")
        self.image_dimensions_label.pack(pady=10)

        # Définir les points de départ et d'arrivée
        tk.Label(self.menu_frame, text="Point de départ (x, y):", bg="lightgray").pack(pady=10)
        start_frame = tk.Frame(self.menu_frame, bg="lightgray")
        start_frame.pack(pady=5)
        self.start_x_entry = tk.Entry(start_frame, width=5)
        self.start_x_entry.pack(side=tk.LEFT, padx=5)
        self.start_y_entry = tk.Entry(start_frame, width=5)
        self.start_y_entry.pack(side=tk.LEFT, padx=5)
        tk.Button(self.menu_frame, text="Définir départ", command=self.set_start_point).pack(pady=5)

        tk.Label(self.menu_frame, text="Point d'arrivée (x, y):", bg="lightgray").pack(pady=10)
        end_frame = tk.Frame(self.menu_frame, bg="lightgray")
        end_frame.pack(pady=5)
        self.end_x_entry = tk.Entry(end_frame, width=5)
        self.end_x_entry.pack(side=tk.LEFT, padx=5)
        self.end_y_entry = tk.Entry(end_frame, width=5)
        self.end_y_entry.pack(side=tk.LEFT, padx=5)
        tk.Button(self.menu_frame, text="Définir arrivée", command=self.set_end_point).pack(pady=5)

        # Bouton pour générer le chemin
        tk.Button(self.menu_frame, text="Générer le chemin", command=self.calculate_and_draw_path).pack(pady=20)

        # Affichage du temps d'exécution
        self.execution_time_label = tk.Label(self.menu_frame, text="Temps: 0.00s", bg="lightgray")
        self.execution_time_label.pack(pady=10)

        # Nouveau label pour afficher le nombre de sommets visités
        self.visited_label = tk.Label(self.menu_frame, text="Sommets visités: 0", bg="lightgray")
        self.visited_label.pack(pady=10)

        # Bouton pour nettoyer l'image
        tk.Button(self.menu_frame, text="Nettoyer l'image", command=self.clear_canvas).pack(pady=10)

        # Bouton pour réinitialiser les points de départ et d'arrivée
        tk.Button(self.menu_frame, text="Réinitialiser points", command=self.reset_points).pack(pady=10)

    def load_image(self):
        """Charge l'image et gère le graphe."""
        if not self.image_path_entry.get():
            self.image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
            self.image_path_entry.insert(0, self.image_path)
        else:
            self.image_path = self.image_path_entry.get()

        if self.image_path:
            # Charger l'image et préparer le graphe
            self.pixels, self.largeur, self.hauteur = load_image(self.image_path)
            self.graphe = image_to_graphe(self.pixels, self.largeur, self.hauteur)

            # Affichage de l'image
            self.image = Image.open(self.image_path).convert("RGB")
            self.photo = ImageTk.PhotoImage(self.image)
            self.canvas.config(width=self.largeur, height=self.hauteur)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
            print("Image et graphe chargés avec succès.")

            self.image_dimensions_label.config(text=f"Dimensions: {self.largeur} x {self.hauteur}")

    def set_start_point(self):
        """Définit le point de départ, uniquement si aucun point de départ n'est déjà défini."""
        if self.sommet_depart is not None:
            messagebox.showerror("Erreur", "Le point de départ est déjà défini.")
            return

        # Récupérer les coordonnées du point de départ
        x = self.start_x_entry.get()
        y = self.start_y_entry.get()

        if not x.isdigit() or not y.isdigit():  # Vérifier si les coordonnées sont des nombres
            messagebox.showerror("Erreur", "Veuillez entrer des coordonnées valides.")
            return

        x, y = int(x), int(y)

        if 0 <= x < self.largeur and 0 <= y < self.hauteur:  # Vérifier si les coordonnées sont dans l'image
            self.sommet_depart = y * self.largeur + x
            self.highlight_pixel(x, y, "green", "start")
        else:
            messagebox.showerror("Erreur", "Coordonnées hors limites pour le point de départ.")

    def set_end_point(self):
        """Définit le point d'arrivée, uniquement si aucun point d'arrivée n'est déjà défini."""
        if self.sommet_arrivee is not None:
            messagebox.showerror("Erreur", "Le point d'arrivée est déjà défini.")
            return

        # Récupérer les coordonnées du point d'arrivée
        x = self.end_x_entry.get()
        y = self.end_y_entry.get()

        if not x.isdigit() or not y.isdigit():  # Vérifier si les coordonnées sont des nombres
            messagebox.showerror("Erreur", "Veuillez entrer des coordonnées valides.")
            return

        x, y = int(x), int(y)

        if 0 <= x < self.largeur and 0 <= y < self.hauteur:  # Vérifier si les coordonnées sont dans l'image
            self.sommet_arrivee = y * self.largeur + x
            self.highlight_pixel(x, y, "red", "end")
        else:
            messagebox.showerror("Erreur", "Coordonnées hors limites pour le point d'arrivée.")

    def calculate_and_draw_path(self):
        """Calcule et dessine le chemin le plus court."""
        if self.sommet_depart is None or self.sommet_arrivee is None:
            messagebox.showerror("Erreur", "Veuillez définir les points de départ et d'arrivée.")
            return

        start_time = time.time()

        # Utiliser l'algorithme de Dijkstra pour trouver le chemin
        chemin, number_tries = self.graphe.dijkstra(self.sommet_depart, self.sommet_arrivee)

         # Dessiner le chemin petit à petit
        for i, sommet in enumerate(chemin):
            x = sommet % self.largeur
            y = sommet // self.largeur

            # Dessiner un petit carré pour chaque sommet du chemin
            size = 1  # Taille du carré
            self.canvas.create_rectangle(x, y, x + size, y + size, fill="blue", outline="blue", tags="path")
        
            # Ajouter un délai pour l'animation (affichage progressif)
            self.canvas.update()  # Met à jour le canevas
            time.sleep(0.01)  # Petite pause pour voir l'animation

          
        # Calcul du temps d'exécution
        execution_time = time.time() - start_time
        self.execution_time_label.config(text=f"Temps: {execution_time:.2f}s")

        # Afficher le nombre de sommets visités
        self.visited_label.config(text=f"Sommets visités: {number_tries}")

        print(f"Chemin trouvé en {execution_time:.2f} secondes avec {number_tries} sommets visités.")

    def highlight_pixel(self, x, y, color, tag):
        """Met en évidence un pixel avec une taille plus visible."""
        size = 1  # Taille du carré pour une meilleure visibilité
        self.canvas.create_rectangle(x, y, x + size, y + size, fill=color, outline=color, tags=tag)



    def clear_canvas(self):
        """Nettoie l'image et réinitialise les paramètres."""
        self.canvas.delete("path")
        self.canvas.delete("start")
        self.canvas.delete("end")
        self.sommet_depart = None
        self.sommet_arrivee = None
        self.execution_time_label.config(text="Temps: 0.00s")
        self.visited_label.config(text="Sommets visités: 0")

        # Réinitialiser le graphe
        if self.pixels is not None:
            self.graphe = image_to_graphe(self.pixels, self.largeur, self.hauteur)

    def reset_points(self):
        """Réinitialise les points de départ et d'arrivée."""
        self.sommet_depart = None
        self.sommet_arrivee = None
        self.canvas.delete("start")
        self.canvas.delete("end")
        self.execution_time_label.config(text="Temps: 0.00s")
        self.visited_label.config(text="Sommets visités: 0")
