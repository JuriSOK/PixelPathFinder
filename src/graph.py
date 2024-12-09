class Arete:
    """
    Classe représentant une arête dans un graphe.
    """
    def __init__(self, src, dest, poids):
        """
        Constructeur de la classe Arete.
        
        :param source: Le sommet de départ de l'arête.
        :param destination: Le sommet d'arrivée de l'arête.
        :param poids: Le poids de l'arête.
        """
        self.source = src
        self.destination = dest
        self.poids = poids


class Sommet:
    """
    Classe représentant un sommet dans un graphe.
    """
    
    def __init__(self, num, indivTime=float('inf')): 
        """
        Constructeur de la classe Sommet.
        
        :param num: L'identifiant unique du sommet dans le graphe.
        :param indivTime: Le coût individuel du sommet. 
        Par défaut, il est défini à l'infini.
        (le sommet est inaccessible au départ dans l'algorithme de Dijkstra).
        """
        self.indivTime = indivTime
        self.timeFromSource = float('inf') 
        self.prev = None  
        self.liste_adj = []  
        self.num = num  

    def ajouter_voisin(self, arete):
        """
        La méthode permet d'ajouter une arête à la liste des voisins (liste d'adjacence) d'un sommet.
        
        :param arete: L'arête à ajouter. 
        """
        self.liste_adj.append(arete)

class Graphe:
    """
    Classe représentant un graphe.
    """
    def __init__(self):
        """
        Constructeur de la classe Graphe.
        Il initialise un graphe vide avec une liste de sommets et un compteur pour définir le numéro des sommets.
        """
        self.liste_sommet = []  
        self.num_v = 0  

    def ajouter_sommet(self, indivTime=float('inf')):
        """
        La méthode permet d'ajouter un sommet avec un temps individuel (indivTime) à la liste des sommets du graphe.
        
        :param indivTime: Le temps individuel associé au sommet (qui sera utilisé dans l'algorithme de Dijkstra).
        """
        sommet = Sommet(self.num_v, indivTime)
        self.liste_sommet.append(sommet)
        self.num_v += 1

    def ajouter_arete(self, source, destination, poids):
        """
        La méthode permet d'ajouter une arête entre deux sommets spécifiés par leurs indices `source` et `destination`, avec un poids donné.
        
        :param source: Le sommet de départ de l'arête.
        :param destination: Le sommet d'arrivée de l'arête.
        :param poids: Le poids de l'arête.
        """
        arete = Arete(source, destination, poids)
        self.liste_sommet[source].ajouter_voisin(arete)