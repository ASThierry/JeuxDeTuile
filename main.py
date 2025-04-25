from PySide6.QtWidgets import QApplication
from Controlleur.loopgame import Game

if __name__ == '__main__':
    app = QApplication([])
    play = Game()
    play.show()
    app.exec()
