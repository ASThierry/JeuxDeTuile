from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QMessageBox
from src.Plateau import Plateau
from src.Tuile import Tuile
import os


class Game(QWidget):
    """
    Fenêtre principale du jeu qui contient le plateau et le bouton de vérification
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Jeu des Tuyaux")
        self.setFixedSize(600, 650)  # Taille fixe pour la fenêtre

        # Crée le plateau de jeu
        self.plateau = Plateau()

        # Liste des images pour chaque tuile (16 tuiles)
        images = [
            "tuyaux2.png", "tuyaux2.png", "tuyaux4.png", "tuyaux0.png",
            "tuyaux0.png", "tuyaux0.png", "tuyaux2.png", "tuyaux0.png",
            "tuyaux0.png", "tuyaux0.png", "tuyaux2.png", "tuyaux0.png",
            "tuyaux0.png", "tuyaux0.png", "tuyaux4.png", "tuyaux2.png"
        ]

        # Ajoute les tuiles au plateau
        index = 0
        for ligne in range(4):
            for colonne in range(4):
                if index < len(images):
                    # Crée le chemin complet vers l'image
                    chemin = os.path.join("images", images[index])
                    tuile = Tuile(chemin)
                    self.plateau.ajouter_tuile(tuile, ligne, colonne)
                    index += 1

        # Bouton pour vérifier la solution
        btn_verifier = QPushButton("Vérifier")
        btn_verifier.clicked.connect(self.verifier_solution)
        btn_verifier.setFixedHeight(40)  # Hauteur fixe pour le bouton

        # Organisation de l'interface
        layout = QVBoxLayout()
        layout.addWidget(self.plateau)
        layout.addWidget(btn_verifier)
        self.setLayout(layout)

    def verifier_solution(self):
        """
        Vérifie si le joueur a gagné et affiche un message
        """
        if self.plateau.verifier_victoire():
            QMessageBox.information(self,'Victoire',"Félicitations Vous avez gagné !")
        else:
            QMessageBox.warning(self, "Essaie encore", "Les tuyaux ne sont pas bien connectés !")