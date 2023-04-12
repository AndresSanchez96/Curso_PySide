from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QLabel, QApplication, QCheckBox


class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Componentes')
        # Creamos un nuevo Checkbox
        checkbox = QCheckBox('Este es un checkbox')
        # activamos el tercer estado
        checkbox.setTristate(True)
        # Concectar la señal de cambio de componente
        checkbox.stateChanged.connect(self.mostrar_estado)
        # Publicamos este componente
        self.setCentralWidget(checkbox)

    def mostrar_estado(self, estado):
        print(f'Estado checkbox: {estado}')
        # Trabajamos con las constantes
        if estado == Qt.Checked:
            print('CheckBox Encendido')
        elif estado == Qt.PartiallyChecked:
            print('CheckBox sin estado o parcialmente checado')
        elif estado == Qt.Unchecked:
            print('CheckBoc apagado')

if __name__ == '__main__':
    app = QApplication([])
    ventana = Componentes()
    ventana.show()
    app.exec()