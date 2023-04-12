# Signals and Slots
import sys

from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget


class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Signals y Slots')
        #self.resize(300, 300)
        self.setFixedSize(400, 200)
        # Definimos la etiqueta y la linea de edicion
        self.etiqueta = QLabel()
        self.entrada_texto = QLineEdit()
        # Conectar el widget de entrada de texto con la etiqueta
        # La señal es textChanged, el slot es setText
        self.entrada_texto.textChanged.connect(self.etiqueta.setText)
        # Publicamos los componentes usando un layout
        layout = QVBoxLayout()
        layout.addWidget(self.entrada_texto)
        layout.addWidget(self.etiqueta)
        # Crear un contenedor para publicar el layout
        contenedor = QWidget()
        contenedor.setLayout(layout)
        # Publicamos el contenedor
        self.setCentralWidget(contenedor)


if __name__ == '__main__':
    # Creamos el objeto app
    app = QApplication([])
    # Creamos una instancia de nuetra clase
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())