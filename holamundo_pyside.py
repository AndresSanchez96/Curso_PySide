import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow

# Esta es la clase base de QT (PySide)
# Esta clase se encarga de procesar los eventos (Event Loop)
app = QApplication()
# Crear un objeto ventana
# Cualquier componente puede ser una ventana en PySide
#ventana = QPushButton('Boton PySide')
#ventana = QWidget()
ventana = QMainWindow() # Ventana Principal
# Modificar cuestiones de la ventana
ventana.setWindowTitle('Hola mundo con PySide')
# Modificamos el tamaño de la ventana
ventana.resize(600, 400)
# Mostrar la ventana
ventana.show()
# Se ejecuta la app
sys.exit(app.exec())