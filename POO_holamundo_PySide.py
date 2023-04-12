import sys

from PySide6.QtCore import QSize
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton


class VentanaPySide(QMainWindow):
    def __init__(self):
        # LLamamos al metodo init de la casa padre
        super().__init__()

        self.setWindowTitle('POO con PySide')
        #self.resize(600, 400)
        # Ventana fija, no se puede mod el tamaño
        self.setFixedSize(QSize(600, 400))

        # Creamos el metodo de componenetes
        self._agregar_componentes()

    def _agregar_componentes(self):
        # Agregamos un menu
        menu = self.menuBar()
        menu_archivo = menu.addMenu('Archivo')
        # Agregamos algunas opciones al menu
        accion_nuevo = QAction('Nuevo', self)
        menu_archivo.addAction(accion_nuevo)
        # Agregamos un texto a la barra de estado
        accion_nuevo.setStatusTip('Nuevo Archivo')
        # Agregamos un mensaje en la barra de estado
        self.statusBar().showMessage('Informacion de la barra de estado')
        # Agregamos un boton
        boton = QPushButton('Nuevo Boton')
        # Publicamos el boton en la ventana
        self.setCentralWidget(boton)

if __name__ == '__main__':
    app = QApplication([])
    # Creamos un objeto de tipo ventana
    ventana = VentanaPySide()
    ventana.show()
    # Ejecutamos la ventana
    sys.exit(app.exec())