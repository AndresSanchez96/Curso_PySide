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
        dialogo.setWindowTitle('Dialogo con pregunta')
        dialogo.setText('Ventana de dialogo con pregunta')
        # Agregamos los botones de la respuesa de la pregunta
        dialogo.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        # Agregamos un icono a la ventana de dialogo
        dialogo.setIcon(QMessageBox.Question)
        valor_retornado = dialogo.exec()
        # Impimimos el valor retornado
        print(f'Valor retornado: {valor_retornado}')

        if valor_retornado == QMessageBox.Yes:
            print('Regreso el valor de Yes')
        else:
            print('Regrese un valor de No')


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()