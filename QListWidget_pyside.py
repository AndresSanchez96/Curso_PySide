from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QLabel, QApplication, QCheckBox, QComboBox, QListWidget


class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Componentes')
        # Componente QListWidget se parece al comobobox
        lista = QListWidget()
        # Agregamos elementos
        lista.addItem('Uno')
        lista.addItems(['Dos', 'Tres'])
        # Monitoramos el cambio del elemento seleccionado, tanto el elementos como e texto 
        lista.currentItemChanged.connect(self.cambio_elemento)
        lista.currentTextChanged.connect(self.cambio_texto)
        

        # Publicamos este componente
        self.setCentralWidget(lista)

    def cambio_elemento(self, nuevo_elemento):
        print(f'Nuevo elemento seleccionado: {nuevo_elemento.text()}')

    def cambio_texto(self, nuevo_texto):
        print(f'Nuevo texto selexionado: {nuevo_texto}')

if __name__ == '__main__':
    app = QApplication([])
    ventana = Componentes()
    ventana.show()
    app.exec()