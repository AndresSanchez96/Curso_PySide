from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QLabel, QApplication, QCheckBox, QComboBox


class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Componentes')
        # Creamos un nuevo componente ComboBox ( drop down list)
        combobox = QComboBox()
        # Agregamos elementos
        combobox.addItem('Uno')
        combobox.addItems(['Dos', 'Tres'])
        # Monitoreamos el cambio de elementos seleccionado,
        # tanto de indice como de texto
        combobox.currentIndexChanged.connect(self.cambio_indice)
        combobox.currentTextChanged.connect(self.cambio_texto)
        # hacemos editable el combobox
        combobox.setEditable(True)
        # Especificamos la politica de inserccion
        # NO inserta nada
        #combobox.setInsertPolicy(QComboBox.NoInsert)
        # Agregar al inicio del combobox
        #combobox.setInsertPolicy(QComboBox.InsertAtTop)
        # Modifica el elemento actual
        #combobox.setInsertPolicy(QComboBox.InsertAtCurrent)
        # Insertar al final del combobox
        #combobox.setInsertPolicy(QComboBox.InsertAtBottom)
        # INsertar antes del elemento actual
        #combobox.setInsertPolicy(QComboBox.InsertBeforeCurrent)
        # Insertar despues del elemento actual
        #combobox.setInsertPolicy(QComboBox.InsertAfterCurrent)
        # Agregar alfabeticamente
        combobox.setInsertPolicy(QComboBox.InsertAlphabetically)

        # Limitar cuantos elementos agramos al combobox
        combobox.setMaxCount(6)

        # Publicamos este componente
        self.setCentralWidget(combobox)

    def cambio_indice(self, nuevo_indice):
        print(f'Nuevo indice seleccionado: {nuevo_indice}')

    def cambio_texto(self, nuevo_texto):
        print(f'Nuevo texto selexionado: {nuevo_texto}')

if __name__ == '__main__':
    app = QApplication([])
    ventana = Componentes()
    ventana.show()
    app.exec()