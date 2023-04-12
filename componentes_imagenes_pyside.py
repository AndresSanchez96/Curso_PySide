from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QLabel, QApplication


class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Componentes')
        self.setFixedSize(500, 600)
        # Creamos un label
        label = QLabel('Hola')
        label.setPixmap(QPixmap('layla.jpg'))
        label.setScaledContents(True)
        # Publicamos el label
        self.setCentralWidget(label)

if __name__ == '__main__':
    app = QApplication([])
    ventana = Componentes()
    ventana.show()
    app.exec()