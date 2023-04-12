from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QDialog, QDialogButtonBox, QVBoxLayout, QLabel


class VentanaDialogo(QDialog):
    def __init__(self, padre = None):
        super().__init__(padre)
        self.setWindowTitle('Ventana de dialogo')
        # Agregar un boton de cancelar y aceptar
        botones = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.botones_dialogo = QDialogButtonBox(botones)
        self.botones_dialogo.accepted.connect(self.accept)
        self.botones_dialogo.rejected.connect(self.reject)

        # Creamos un layout para publicar los botones
        self.layout = QVBoxLayout()
        mensaje = QLabel('Presiona alguno de los botones')
        self.layout.addWidget(mensaje)
        self.layout.addWidget(self.botones_dialogo)
        self.setLayout(self.layout)

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        # Agregamos un boton
        boton = QPushButton('Mostrar dialogo')
        boton.clicked.connect(self.click_boton)

        # Publicamos el boton
        self.setCentralWidget(boton)

    def click_boton(self, s):
        print(f'Click Sobre Boton: {s}')
       # Creamos el dialogo
        dialogo = VentanaDialogo(self)
        valor_retornado = dialogo.exec()
        print(f'Valor Retornado {valor_retornado}')
        if valor_retornado:
            print('Se presiono OK')
        else:
            print('Se preciono Cancel')


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()