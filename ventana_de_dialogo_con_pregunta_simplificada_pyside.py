from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QDialog, QDialogButtonBox, QVBoxLayout, QLabel, \
    QMessageBox


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
        #dialogo = QMessageBox.question(self, 'Pregunta', 'Ventana con pregunta')
        dialogo = QMessageBox.critical(self, 'Problema critico', 'Ventana con prbolema critico',
                                       buttons=QMessageBox.Discard |
                                       QMessageBox.NoToAll |
                                       QMessageBox.Ignore,
                                       defaultButton=QMessageBox.Discard)
        if dialogo == QMessageBox.Ok:
            print('Regreso el valor de OK')
        else:
            print('Regrese un valor distinto de OK')


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()