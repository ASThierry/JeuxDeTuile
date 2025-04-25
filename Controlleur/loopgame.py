from PySide6.QtWidgets import QWidget
from src.Plateau import Plateau
from src.Tuile import Tuile

class Game(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mon Jeu")
        board = Plateau()
        tile1 = Tuile('images/img1.jpg')
        tile2 = Tuile('images/img1.jpg')
        tile3 = Tuile('images/img1.jpg')
        tile4 = Tuile('images/img1.jpg')

        tile5 = Tuile('images/img1.jpg')
        tile6 = Tuile('images/img1.jpg')
        tile7 = Tuile('images/img1.jpg')
        tile8 = Tuile('images/img1.jpg')

        tile9 = Tuile('images/img1.jpg')
        tile10 = Tuile('images/img1.jpg')
        tile11 = Tuile('images/img1.jpg')
        tile12 = Tuile('images/img1.jpg')

        tile13 = Tuile('images/img1.jpg')
        tile14 = Tuile('images/img1.jpg')
        tile15 = Tuile('images/img1.jpg')
        tile16 = Tuile('images/img1.jpg')

        board.ajouter_tuile(tile1,0,0)
        board.ajouter_tuile(tile2,0,1)
        board.ajouter_tuile(tile3, 0, 2)
        board.ajouter_tuile(tile4, 0, 3)
        board.ajouter_tuile(tile5, 1, 0)
        board.ajouter_tuile(tile6, 1, 1)
        board.ajouter_tuile(tile7, 1, 2)
        board.ajouter_tuile(tile8, 1, 3)
        board.ajouter_tuile(tile9, 2, 0)
        board.ajouter_tuile(tile10, 2, 1)
        board.ajouter_tuile(tile11, 2, 2)
        board.ajouter_tuile(tile12, 2, 3)
        board.ajouter_tuile(tile13, 3, 0)
        board.ajouter_tuile(tile14, 3, 1)
        board.ajouter_tuile(tile15, 3, 2)
        board.ajouter_tuile(tile16, 3, 3)

        self.setLayout(board.layout)
