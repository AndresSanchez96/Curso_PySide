from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QWidget, QMainWindow, QApplication, QTabWidget


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

        # Creamos el componente tab
        tabulador = QTabWidget()
        # Posicion de las etiquetas del tabulador
        tabulador.setTabPosition(QTabWidget.North)
        # Indicamos si queremos que se muevan las etiquetas del tabulador
        tabulador.setMovable(True)

        # Agregamos los colores a cada tabulador
        tabulador.addTab(Color('red'), 'Rojo')
        tabulador.addTab(Color('yellow'), 'Amarillo')
        tabulador.addTab(Color('purple'), 'Morado')

        # El componente se expande para cubrir el tamaño disponible
        self.setCentralWidget(tabulador)

if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()