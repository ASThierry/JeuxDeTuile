from PySide6.QtWidgets import QWidget, QGridLayout

class Plateau(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QGridLayout()
        self.setLayout(self.layout)

    def ajouter_tuile(self, tuile, x=0, y=0):
        self.layout.addWidget(tuile, x, y)
