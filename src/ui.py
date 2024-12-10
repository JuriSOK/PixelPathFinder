from PIL import Image, ImageTk
import tkinter as tk

def afficher_chemin(image_path, chemin, sommet_depart, sommet_arrivee, largeur, hauteur):
    """
    Affiche l'image avec les points de départ et d'arrivée en rouge, et le chemin en bleu.
    """
    # Configuration de la fenêtre
    root = tk.Tk()
    root.title("Chemin le plus court")
    canvas = tk.Canvas(root, width=largeur, height=hauteur)
    canvas.pack()

    # Charger l'image d'origine
    img = Image.open(image_path)
    photo = ImageTk.PhotoImage(img)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)


    # Dessiner le sommet de départ et d'arrivée en rouge
    x_depart = sommet_depart % largeur
    y_depart = sommet_depart // largeur
    canvas.create_rectangle(
        x_depart - 3, y_depart - 3, x_depart + 3, y_depart + 3, fill="green", outline="green"
    )

    x_arrivee = sommet_arrivee % largeur
    y_arrivee = sommet_arrivee // largeur
    canvas.create_rectangle(
        x_arrivee - 3, y_arrivee - 3, x_arrivee + 3, y_arrivee + 3, fill="green", outline="green"
    )

    # Dessiner le chemin en bleu
    for pos in chemin:
        x = pos % largeur
        y = pos // largeur
        canvas.create_oval(
            x - 1, y - 1, x + 1, y + 1, fill="blue", outline="blue"
        )

    root.mainloop()
