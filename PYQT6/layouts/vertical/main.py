import sys
import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox)

class Mainwindow(QWidget):

    def __init__(self):
        super().__init__()
        self.inicializarUI()
    
    def inicializarUI(self):
        self.setMinimumHeight(200)
        self.setFixedWidth(200)
        self.setWindowTitle("Layout Vertical")
        self.generar_form()
        self.show()
    
    def generar_form(self):
        button = QPushButton("Boton #1")
        button1 = QPushButton("Boton #2")
        button2 = QPushButton("Boton #3")
        button3 = QPushButton("Boton #4")

        button.clicked.connect(self.imprimir_nombre_boton)
        button1.clicked.connect(self.imprimir_nombre_boton)
        button2.clicked.connect(self.imprimir_nombre_boton)
        button3.clicked.connect(self.imprimir_nombre_boton)

        layout = QVBoxLayout()
        layout.addWidget(button)
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)

        self.setLayout(layout)
    
    def imprimir_nombre_boton(self):
        boton = self.sender()
        QMessageBox.information(self, 'Boton Push',
                                f'Se le dio click al boton {boton.text()}',
                                QMessageBox.StandardButton.Ok,
                                QMessageBox.StandardButton.Ok)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Mainwindow()
    sys.exit(app.exec())