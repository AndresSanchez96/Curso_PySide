from PySide6.QtWidgets import QMainWindow, QApplication, QSpinBox, QDoubleSpinBox


class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Componentes')
        # QSpinBox para seleccionar un valor numerico entero
        #numero = QSpinBox()

        # QDoubkeSpinBox es para valores flotantes
        numero = QDoubleSpinBox()

        # Establecer un valor max y min
        #numero.setMinimum(-5)
        #numero.setMaximum(8)
        numero.setRange(-5.5, 8.8)

        # Agregar prefijos y subfijos
        numero.setPrefix('$ ')
        numero.setSuffix('c')

        # establecemos el salto o step
        numero.setSingleStep(.5)

        # Nos conectamos al evento o señal de cambio de valor
        # Envia el valor numero (numerico)
        numero.valueChanged.connect(self.cambio_valor)
        # Envia el valor en texto incluyendo prefijo y subfijo
        numero.textChanged.connect(self.cambio_texto)

        # Publicamos este componente
        self.setCentralWidget(numero)

    def cambio_valor(self, nuevo_valor):
        print(f'Nuevo valor: {nuevo_valor} ')

    def cambio_texto(self, nuevo_texto):
        print(f'Nuevo texto: {nuevo_texto}')


if __name__ == '__main__':
    app = QApplication([])
    ventana = Componentes()
    ventana.show()
    app.exec()