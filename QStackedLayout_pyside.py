from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QWidget, QMainWindow, QApplication, QVBoxLayout, QHBoxLayout, QGridLayout, QStackedLayout


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

        # Layout QStackedLayout (apilado encima del otro)
        layout = QStackedLayout()
        # Por default solo se visualiza el primer widget agregado
        layout.addWidget(Color('red'))
        layout.addWidget(Color('green'))
        layout.setCurrentIndex(1)

        # Se publica el layout mas externo creando un componente generico
        componente = QWidget()
        componente.setLayout(layout)

        # El componente se expande para cubrir el tamaño disponible
        self.setCentralWidget(componente)

if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()