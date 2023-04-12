from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QWidget, QMainWindow, QApplication, QVBoxLayout, QHBoxLayout


class Color(QWidget):
    def __init__(self, nuevo_color):
        super().__init__()
        # Indicamos que se puede agregar un color de fondo
        self.setAutoFillBackground(True)
        paletaColores = self.palette()
        # Creamos el componente de color de fondo aplicando el nuevo color
        paletaColores.setColor(QPalette.Window, QColor(nuevo_color))
        # Aplicamos el nuevo color al componente
        self.setPalette(paletaColores)

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Layouts en Pyside')

        # Anidar layouts (layout dentro de otro layout)
        # Creamos el primer layout hotizontal y despues uno vertical
        layout_horizontal = QHBoxLayout()
        layout_vertical = QVBoxLayout()

        # Agregamos espacion el layout vertical
        layout_vertical.setContentsMargins(5, 10, 5, 10)
        layout_vertical.setSpacing(20)

        # Agregamos espacion el layout horizontal
        layout_horizontal.setContentsMargins(10, 10, 10, 10)
        layout_horizontal.setSpacing(30)

        # Agegamos algunos widgets al layout_vertical
        layout_vertical.addWidget(Color('red'))
        layout_vertical.addWidget(Color('green'))
        layout_vertical.addWidget(Color('blue'))

        # Agregamos el layout vertical dentro del layout horizontal
        # Es decir se agrega de manera anidada
        layout_horizontal.addLayout(layout_vertical)
        # Agregamos mas eelementos al layout horizontal
        layout_horizontal.addWidget(Color('yellow'))
        layout_horizontal.addWidget(Color('purple'))

        # Se publica el layout mas externo creando un componente generico
        componente = QWidget()
        componente.setLayout(layout_horizontal)

        # El componente se expande para cubrir el tamaño disponible
        self.setCentralWidget(componente)

if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()