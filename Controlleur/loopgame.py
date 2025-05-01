from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout
from src.Plateau import Plateau
from src.Tuile import Tuile

class Game(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Jeu de tuiles")

        self.plateau = Plateau()

        images = [
            "images/tuyaux2.png", "images/tuyaux2.png", "images/tuyaux4.png", "images/tuyaux0.jpg",
            "images/tuyaux0.jpg", "images/tuyaux0.jpg", "images/tuyaux2.png", "images/tuyaux0.jpg",
            "images/tuyaux0.jpg", "images/tuyaux0.jpg", "images/tuyaux2.png", "images/tuyaux0.jpg",
            "images/tuyaux0.jpg", "images/tuyaux0.jpg", "images/tuyaux4.png", "images/tuyaux2.png"
        ]

        index = 0
        for x in range(4):
            for y in range(4):
                if index < len(images):
                    tuile = Tuile(images[index])
                    self.plateau.ajouter_tuile(tuile, x, y)
                    index += 1

        bouton = QPushButton("Vérifier la victoire")
        bouton.clicked.connect(self.verifier)

        layout = QVBoxLayout()
        layout.addLayout(self.plateau.layout)
        layout.addWidget(bouton)
        self.setLayout(layout)

    def verifier(self):
        if self.plateau.verifier_victoire():
            print("Vous avez gagné !")
        else:
            print(" vous n'avez pas encore la bonne structure!")
