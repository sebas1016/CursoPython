import sys
import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import (QApplication,QWidget,QLabel,QLineEdit,QPushButton,QHBoxLayout)

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.inicializarUI()

    def inicializarUI(self):
        self.setMinimumWidth(600)
        self.setFixedHeight(80)
        self.setWindowTitle("Layout Horizontal")
        self.generar_form()
        self.show()
    
    def generar_form(self):
        email_label = QLabel('Email')
        email_input = QLineEdit()
        send_button = QPushButton("Enviar")
        layout = QHBoxLayout()
        layout.addWidget(email_label)
        layout.addWidget(email_input)
        layout.addWidget(send_button)
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())