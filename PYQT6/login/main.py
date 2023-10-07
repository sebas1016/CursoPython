import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import QWidget, QLabel, QMessageBox
from PyQt6.QtGui import QPixmap

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()
    
    def inicializarUI(self):
        self.setGeometry(100,100,500,500)
        self.setWindowTitle("Ventana Principal")
        self.generar_contenido()

    def generar_contenido(self):
        imagen_path = 'login\main.jpg'

        try:
            with open(imagen_path):
                image_label = QLabel(self)
                image_label.setPixmap(QPixmap(imagen_path))

        except FileNotFoundError as e:
            QMessageBox.warning(self, 'Error',
                                f'Error en el main view {e}',
                                QMessageBox.StandardButton.Close,
                                QMessageBox.StandardButton.Close)