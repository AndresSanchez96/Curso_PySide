# Signals and Slots
import sys

from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton


class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Signals y Slots')
        self.resize(300, 300)
        # Boton
        self.boton = QPushButton('Click aqui')
        # Asociamos la señal de click al slot evento_click
        self.boton.clicked.connect(self.evento_click)
        # Conectar a la señal de cambio de titulo
        self.windowTitleChanged.connect(self.cambio_titulo_aplicacion)
        # Publicamos el boton
        self.setCentralWidget(self.boton)


    def evento_click(self):
        # Cambiar el texto del boton y el titulo de la ventana
        self.boton.setText('Nuevo texto boton')
        self.boton.setEnabled(False)
        self.setWindowTitle('Nuevo titulo de la aplicacion')

    def cambio_titulo_aplicacion(self, nuevo_titulo):
        print(f'Nuevo titulo de la aplicacion: {nuevo_titulo}')



if __name__ == '__main__':
    # Creamos el objeto app
    app = QApplication([])
    # Creamos una instancia de nuetra clase
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())