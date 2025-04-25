from PySide6.QtWidgets import QPushButton
from PySide6.QtGui import QIcon, QPixmap, QTransform
from PySide6.QtCore import QSize

class Tuile(QPushButton):
    def __init__(self, chemin_image):
        super().__init__()

        # On garde le chemin vers l'image
        self.chemin_image = chemin_image

        # On commence avec un angle de 0 degré (pas de rotation)
        self.angle = 0

        # On charge l'image depuis le fichier
        self.image_originale = QPixmap(self.chemin_image)

        # On met l'image comme icône du bouton
        self.setIcon(QIcon(self.image_originale))

        # On définit la taille de l'icône (et du bouton)
        taille = QSize(150, 150)
        self.setIconSize(taille)
        self.setFixedSize(taille)

        # Quand on clique sur le bouton, on appelle la fonction pour tourner l'image
        self.clicked.connect(self.tourner_image)

    def tourner_image(self):
        # À chaque clic, on ajoute 90 degrés à l'angle
        self.angle = (self.angle + 90) % 360

        # On crée une transformation (rotation)
        transformation = QTransform().rotate(self.angle)

        # On applique la rotation à l'image d'origine
        image_tournee = self.image_originale.transformed(transformation)

        # On met à jour l'image affichée sur le bouton
        self.setIcon(QIcon(image_tournee))
