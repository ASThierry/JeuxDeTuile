from PySide6.QtWidgets import QPushButton
from PySide6.QtGui import QIcon, QPixmap, QTransform
from PySide6.QtCore import QSize


class Tuile(QPushButton):
    """
    Une tuile du jeu qui peut être tournée et qui a des connexions
    """

    def __init__(self, chemin_image):
        super().__init__()

        # Configuration de base
        self.chemin_image = chemin_image
        self.angle = 0  # Angle actuel de rotation (0, 90, 180, 270)
        self.connection = []  # Directions connectées (haut, bas, gauche, droit)

        # Charge l'image
        self.charger_image()

        # Configure l'apparence
        self.setFixedSize(QSize(150, 150))

        # Connecte le clic à la rotation
        self.clicked.connect(self.tourner)

    def charger_image(self):
        """Charge et affiche l'image"""
        try:
            self.image_originale = QPixmap(self.chemin_image)
            self.setIcon(QIcon(self.image_originale))
            self.setIconSize(QSize(150, 150))
            self.mettre_a_jour_connexions()
        except:
            print(f"Erreur: Impossible de charger {self.chemin_image}")

    def tourner(self):
        """Tourne la tuile de 90 degrés"""
        self.angle = (self.angle + 90) % 360
        transform = QTransform().rotate(self.angle)
        image_tournee = self.image_originale.transformed(transform)
        self.setIcon(QIcon(image_tournee))
        self.mettre_a_jour_connexions()

    def mettre_a_jour_connexions(self):
        """Met à jour les connexions selon l'image et l'angle"""
        self.connection.clear()

        # Simplification: on utilise le nom du fichier seulement
        nom_fichier = self.chemin_image.split('/')[-1]

        # Détection des connexions en fonction du type de tuile
        if nom_fichier == "tuyaux2.png":
            if self.angle in [0, 180]:
                self.connection = ["gauche", "droit"]
            else:
                self.connection = ["haut", "bas"]

        elif nom_fichier == "tuyaux4.png":
            if self.angle == 0:
                self.connection = ["gauche", "bas"]
            elif self.angle == 90:
                self.connection = ["haut", "gauche"]
            elif self.angle == 180:
                self.connection = ["haut", "droit"]
            elif self.angle == 270:
                self.connection = ["droit", "bas"]

        elif nom_fichier == "tuyaux1.png":
            # Tuile en T
            if self.angle == 0:
                self.connection = ["haut", "gauche", "droit"]
            elif self.angle == 90:
                self.connection = ["haut", "droit", "bas"]
            elif self.angle == 180:
                self.connection = ["gauche", "droit", "bas"]
            elif self.angle == 270:
                self.connection = ["haut", "gauche", "bas"]

        elif nom_fichier == "tuyaux3.png":
            # Tuile croix (4 connexions)
            self.connection = ["haut", "bas", "gauche", "droit"]

        elif nom_fichier == "tuyaux0.jpg":
            # Tuile vide
            self.connection = []