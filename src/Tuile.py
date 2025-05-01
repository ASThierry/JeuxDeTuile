from PySide6.QtWidgets import QPushButton
from PySide6.QtGui import QIcon, QPixmap, QTransform
from PySide6.QtCore import QSize

class Tuile(QPushButton):
    def __init__(self, chemin_image):
        super().__init__()

        self.chemin_image = chemin_image
        self.angle = 0  # Angle de rotation
        self.connection = []  # Connexions actuelles de la tuile

        # Chargement de l'image d'origine
        self.image_originale = QPixmap(self.chemin_image)

        # Affichage de l'image dans le bouton
        self.setIcon(QIcon(self.image_originale))
        taille = QSize(150, 150)
        self.setIconSize(taille)
        self.setFixedSize(taille)

        # Action au clic : faire tourner l'image
        self.clicked.connect(self.tourner_image)

        # Initialiser les connexions
        self.mettre_a_jour_connexions()

    def tourner_image(self):
        # Rotation de l'angle
        self.angle = (self.angle + 90) % 360

        # Appliquer la rotation à l'image
        transformation = QTransform().rotate(self.angle)
        image_tournee = self.image_originale.transformed(transformation)

        # Afficher l'image tournée
        self.setIcon(QIcon(image_tournee))

        # Mettre à jour les connexions après rotation
        self.mettre_a_jour_connexions()

    def mettre_a_jour_connexions(self):
        #Met à jour la liste des connexions en fonction de l’image et de l’angle.
        self.connection.clear()

        # Tuyau droit : gauche - droite ou haut - bas
        if self.chemin_image == "images/tuyaux2.jpg":
            if self.angle in [0, 180]:
                self.connection += ["gauche", "droit"]
            else:  # 90 ou 270
                self.connection += ["haut", "bas"]

        # Tuyau coudé à a un angle de 90)
        elif self.chemin_image == "images/tuyaux4.jpg":
            if self.angle == 0:
                self.connection += ["gauche", "bas"]
            elif self.angle == 90:
                self.connection += ["gauche", "haut"]
            elif self.angle == 180:
                self.connection += ["haut", "droit"]
            elif self.angle == 270:
                self.connection += ["droit", "bas"]

        elif self.chemin_image == "images/tuyaux1.png":
            if self.angle == 0 :
                self.connection += ["gauche", "droit","haut"]
            elif self.angle == 90 :
                self.connection += ["haut", "bas", "droit"]
            elif self.angle == 180:
                self.connection += ["droit", "gauche", "bas"]
            elif self.angle == 270:
                self.connection += ["haut", "bas", "gauche"]

        # tuyau connecté dans les 4 directions
        elif self.chemin_image == "images/tuyaux3.png":
            self.connection += ["haut", "droit", "bas", "gauche"]

        #image vide
        elif self.chemin_image == "images/tuyaux0.jpg":
            # Aucune connexion
            self.connection = []


