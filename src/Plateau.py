from PySide6.QtWidgets import QWidget, QGridLayout


class Plateau(QWidget):
    """
    Plateau de jeu 4x4 qui gère les tuiles et vérifie les connexions
    """

    def __init__(self):
        super().__init__()

        # Crée une grille 4x4 vide
        self.grille = [[None] * 4 for _ in range(4)]

        # Configure le layout
        self.layout = QGridLayout()
        self.layout.setSpacing(0)  # Pas d'espace entre les tuiles
        self.setLayout(self.layout)

    def ajouter_tuile(self, tuile, ligne, colonne):
        """
        Ajoute une tuile à la position spécifiée
        """
        self.layout.addWidget(tuile, ligne, colonne)
        self.grille[ligne][colonne] = tuile

    def verifier_victoire(self):
        """
        Vérifie si toutes les tuiles sont correctement connectées
        """
        directions = {
            "haut": (-1, 0),
            "bas": (1, 0),
            "gauche": (0, -1),
            "droit": (0, 1)
        }

        oppose = {
            "haut": "bas",
            "bas": "haut",
            "gauche": "droit",
            "droit": "gauche"
        }

        for ligne in range(4):
            for colonne in range(4):
                tuile = self.grille[ligne][colonne]

               # Ignore les cases vides
                if not tuile:
                    continue

                # Vérifie chaque connexion
                for direction in tuile.connection:
                    dl, dc = directions[direction]
                    nl, nc = ligne + dl, colonne + dc

                    # Vérifie si c'est dans la grille
                    if 0 <= nl < 4 and 0 <= nc < 4:
                        voisin = self.grille[nl][nc]
                        if not voisin or oppose[direction] not in voisin.connection:
                            return False
                    else:
                        # Connexion qui sort du plateau
                        return False

        # Toutes les connexions sont bonnes
        return True