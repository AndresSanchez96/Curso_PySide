from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QLabel


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Eventos')
        self.etiqueta = QLabel('Dar click en esta ventana')
        self.setCentralWidget(self.etiqueta)

    def mouseMoveEvent(self, evento):
        self.etiqueta.setText('Evento mouseMoveEvent detectado')

    def mousePressEvent(self, evento):
        #self.etiqueta.setText('Evento mousePressEvent detectado')
        # Preguntamos por el boton del mouse que lanzo el evento
        if evento.button() == Qt.LeftButton:
            self.etiqueta.setText('Evento mousePressEvent Boton Izquierdo')
        elif evento.button() == Qt.MiddleButton:
            self.etiqueta.setText('mousePressEvent Boton Central')
        elif evento.button() == Qt.RightButton:
            self.etiqueta.setText('mousePressEvent Boton Derecho')

    def mouseReleaseEvent(self, evento):
        self.etiqueta.setText('Evento mouseReleaseEvent Detectado')

    def mouseDoubleClickEvent(self, evento):
        self.etiqueta.setText('Evento mouseDoubleClickEvent detectado')

if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()