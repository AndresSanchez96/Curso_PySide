from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QMainWindow, QApplication, QLabel, QToolBar, QStatusBar, QCheckBox


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Barra de Herramientas')
        self.resize(600, 400)
        # Publicamos una etiqueta
        etiqueta = QLabel('Hola')
        etiqueta.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(etiqueta)

        # Creamos la barra de herramientas
        barra = QToolBar('Mi barra de herramientas')
        barra.setIconSize(QSize(16, 16))

        #Configuracion para mostrar la barra de herramientas
        #barra.setToolButtonStyle(Qt.ToolButtonFollowStyle)
        #barra.setToolButtonStyle(Qt.ToolButtonTextOnly)
        #barra.setToolButtonStyle(Qt.ToolButtonIconOnly)
        #barra.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        barra.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.addToolBar(barra)

        # Agregamos un elemento a nuestra barra de herramientas
        boton_nuevo = QAction(QIcon('nuevo.png'), 'Nuevo', self)
        boton_guardar = QAction(QIcon('guardar.png'), 'Guardar', self)

        # Agragamos el boton a la barra
        barra.addAction(boton_nuevo)
        barra.addAction(boton_guardar)

        # Barra de estado
        self.setStatusBar(QStatusBar(self))

        # Mostramos mensajes del boton accion
        boton_nuevo.setStatusTip('Nuevo Archivo')
        boton_guardar.setStatusTip('Guardar Archivo')

        # Configura un slot para el boton de la barra (asociamos el evento click)
        boton_nuevo.triggered.connect(self.click_boton_nuevo)
        boton_guardar.triggered.connect(self.click_boton_guardar)

        # Hacemos checable el boton
        #boton_nuevo.setCheckable(True)

        barra.addSeparator()

        barra.addWidget(QCheckBox())
        barra.addWidget(QLabel('Salir'))

    def click_boton_nuevo(self, s):
        print(f'Nuevo Archivo {s}')

    def click_boton_guardar(self, s):
        print(f'Guardar Archivo {s}')


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()