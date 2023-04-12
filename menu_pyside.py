from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QAction, QIcon, QKeySequence
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

        ## MENUS
        menu = self.menuBar()
        menu_archivo = menu.addMenu('&Archivo')
        menu_archivo.addAction(boton_nuevo)

        # Agregamos una segunda opcion
        menu_archivo.addAction(boton_guardar)

        # agregamos un separador
        menu_archivo.addSeparator()

        # Agregamos una tercera opcion
        boton_salir = QAction('Salir', self)
        menu_archivo.addAction(boton_salir)

        # SubMenu Ayuda
        boton_acerca_de = QAction(QIcon('acerca.png'), 'Acerca De', self)
        menu_ayuda = menu.addMenu('Ayuda')
        menu_ayuda.addAction(boton_acerca_de)
        # Se configura un slot para acerca de }
        boton_acerca_de.triggered.connect(self.click_acerca_de)

        # Agregamos un submenu
        menu_archivo.addMenu(menu_ayuda)

        # CREACION DE ATAJOS PARA EL MENU
        # EJ. COMBINACION DE TECLAS
        #boton_nuevo.setShortcut(QKeySequence('Ctrl+n'))
        boton_nuevo.setShortcut(Qt.CTRL | Qt.Key_N)
        # Atajo para acerca de Ctrl + 1
        boton_acerca_de.setShortcut(Qt.CTRL | Qt.Key_1)
        # Atajo de guardar Ctrl + g
        boton_guardar.setShortcut(Qt.CTRL | Qt.Key_G)



    def click_boton_nuevo(self, s):
        print(f'Nuevo Archivo {s}')

    def click_boton_guardar(self, s):
        print(f'Guardar Archivo {s}')

    def click_acerca_de(self, s):
        print(f'Acerca de... {s}')


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()