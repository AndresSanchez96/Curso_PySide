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
        dialogo = QMessageBox(self)
        dialogo.setWindowTitle('Dialogo siemple')
        dialogo.setText('Ventana de dialogo simple')
        valor_retornado = dialogo.exec()
        # Impimimos el valor retornado
        print(f'Valor retornado: {valor_retornado}')

        if valor_retornado == QMessageBox.Ok:
            print('Regreso el valor de OK')
        else:
            print('Regrese un valor distinto de OK')


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()