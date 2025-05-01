from PySide6.QtWidgets import QWidget, QGridLayout

def direction_opposee(direction):
    sens_opposer = {
        "haut": "bas",
        "bas": "haut",
        "gauche": "droit",
        "droit": "gauche"
    }
    return sens_opposer[direction]

class Plateau(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.grille = [[None for _ in range(4)] for _ in range(4)]

    def ajouter_tuile(self, tuile, x, y):
        self.layout.addWidget(tuile, x, y)
        self.grille[x][y] = tuile

    def verifier_victoire(self):
        for x in range(4):
            for y in range(4):
                tuile = self.grille[x][y]
                if tuile is None:
                    continue

                for direction in tuile.connection:
                    nx, ny = x, y
                    if direction == "haut":
                        nx -= 1
                    elif direction == "bas":
                        nx += 1
                    elif direction == "gauche":
                        ny -= 1
                    elif direction == "droit":
                        ny += 1

                    if 0 <= nx < 4 and 0 <= ny < 4:
                        voisine = self.grille[nx][ny]
                        if voisine is None:
                            return False
                        if direction_opposee(direction) not in voisine.connection:
                            return False
                    else:
                        # Si la connexion sort du plateau : erreur
                        return False
        return True
