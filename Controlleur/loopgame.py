from PySide6.QtWidgets import QWidget
from src.Plateau import Plateau
from src.Tuile import Tuile

class Game(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mon Jeu")
        board = Plateau()
        self.liste_images = [
    "image/anim.jpeg",
    "image/arrie.jpeg",
    "image/arrire.jpeg",
    "image/aura.jpg",
    "image/colored_pencil_sketch.jpg",
    "image/cosmic.jpg",
    "image/demon.png",
    "image/enchanted.jpeg",
    "image/img1.jpg",
    "image/machien.jpg",
    "image/p.jpg",
    "image/papier.png",
    "image/pencil_sketch.jpg",
    "image/roule dessus.png",
    "image/s.png",
    "image/temple.jpg"
]

        index = 0
        for x in range(4):
            for y in range(4):
                if index < len(self.liste_images):
                    icone = Tuile(self.liste_images[index])
                board.ajouter_tuile(icone, x, y)
                index += 1


        self.setLayout(board.layout)
