from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QWidget, QMainWindow, QApplication, QVBoxLayout, QHBoxLayout, QGridLayout, QStackedLayout, \
    QPushButton


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

        #Definimos nuestro layout
        layout_principal = QVBoxLayout()
        layout_botones = QHBoxLayout()
        self.layout_tipo_stack = QStackedLayout()
        # Agregamos los layout hijos al principal
        layout_principal.addLayout(layout_botones)
        layout_principal.addLayout(self.layout_tipo_stack)

        # Creamos los botones del layout botones
        boton_rojo = QPushButton('Rojo')
        boton_azul = QPushButton('Azul')
        boton_amarillo = QPushButton('Amarillo')
        # Publicar este boton en el layout de botones
        layout_botones.addWidget(boton_rojo)
        layout_botones.addWidget(boton_azul)
        layout_botones.addWidget(boton_amarillo)
        # Se publican los colores al layout de tipo stack
        self.layout_tipo_stack.addWidget(Color('red'))
        self.layout_tipo_stack.addWidget(Color('blue'))
        self.layout_tipo_stack.addWidget(Color('yellow'))
        # Se configura los eventos de los botones al presionarlos
        boton_rojo.pressed.connect(lambda: self.activar_tabulador(0))
        boton_azul.pressed.connect(lambda: self.activar_tabulador(1))
        boton_amarillo.pressed.connect(lambda: self.activar_tabulador(2))

        # Se publica el layout mas externo creando un componente generico
        componente = QWidget()
        componente.setLayout(layout_principal)

        # El componente se expande para cubrir el tamaño disponible
        self.setCentralWidget(componente)

    def activar_tabulador(self, indice):
        self.layout_tipo_stack.setCurrentIndex(indice)


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()