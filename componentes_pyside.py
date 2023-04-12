from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QLabel, QApplication


class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Componentes')
        # Creamos un label
        label = QLabel('Hola')
        # Modificamos el valor inicial del label
        label.setText('Saludos')
        # Modificaciones de la fuente de la etiqueta
        fuente = label.font()
        fuente.setPixelSize(25) # Mas grande la fuente
        label.setFont(fuente)
        # Modificar la alineacion del albel
        #label.setAlignment(Qt.AlignCenter)
        label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        # Publicamos el label
        self.setCentralWidget(label)

if __name__ == '__main__':
    app = QApplication([])
    ventana = Componentes()
    ventana.show()
    app.exec()