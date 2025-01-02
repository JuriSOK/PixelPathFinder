# PixelPathFinder

PixelPathFinder est une application interactive utilisant des algorithmes de graphes pour trouver le chemin le plus court entre deux points sur une image. Ce projet a été conçu dans le cadre d'un mini-projet en Algorithmique (L3).

---

## Fonctionnalités principales

- Chargement d'images et transformation en graphes pondérés.
- Visualisation interactive des points de départ et d'arrivée sur une image.
- Génération de chemins les plus courts à l'aide des algorithmes **Dijkstra** et **A***.
- Prise en charge des heuristiques pour A* :
  - Manhattan.
  - Euclidienne.
- Animation du traçage des chemins.
- Affichage des statistiques, notamment :
  - Temps d'exécution.
  - Nombre de sommets visités.
  - Poids total du chemin.
- Nettoyage et réinitialisation faciles des données et de la visualisation.

---

## Structure du projet

### 1. `main.py`
- Point d'entrée principal du projet.
- Instancie et exécute l'interface utilisateur via la classe `PixelPathFinderApp`.

### 2. `ui.py`
- Contient l'interface utilisateur basée sur **Tkinter**.
- Gère les interactions utilisateur, le chargement d'images, et l'affichage des résultats.
- Implémente des fonctionnalités comme :
  - Sélection de l'image à charger.
  - Définition des points de départ et d'arrivée.
  - Sélection de l'algorithme et de l'heuristique.
  - Animation du chemin trouvé.

### 3. `graph.py`
- Implémente la structure de données pour les graphes, incluant :
  - Classes `Sommet` et `Arete` pour représenter les nœuds et les liens.
  - Classe `Graphe` pour gérer les opérations principales sur le graphe.
- Fournit les algorithmes :
  - **Dijkstra** : Trouve le chemin le plus court entre deux sommets.
  - **A*** : Utilise une heuristique pour guider la recherche.

### 4. `img_manager.py`
- Permet de convertir une image en graphe pondéré.
- Les pixels sont traités comme des sommets, et les différences d'intensité entre pixels adjacents déterminent les poids des arêtes.
- Fonctionnalités principales :
  - `load_image()` : Charge une image en niveaux de gris.
  - `image_to_graphe()` : Convertit une image en un graphe pondéré utilisable par les algorithmes.

---

## Installation et exécution

### Prérequis

- Python 3.8 ou supérieur.
- Bibliothèques requises :
  - `Pillow` (pour la manipulation des images).
  - `Tkinter` (inclus avec Python sur la plupart des systèmes).

### Installation

1. Clonez ce dépôt :
   ```bash
   git clone https://github.com/JuriSOK/PixelPathFinder.git
   cd PixelPathFinder
