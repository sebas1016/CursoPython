import sys
import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import(QApplication, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()
    
    def inicializarUI(self):
        self.setGeometry(100,100,400,150)
        self.setWindowTitle("Layout Nested")
        self.generar_formulario()
        self.show()
    
    def generar_formulario(self):
        mensaje_principal = QLabel('Por favor ingrese sus datos')
        nombres_label = QLabel('Nombres:')
        nombres_label.setFixedWidth(60)
        self.nombres_input = QLineEdit()
        apellidos_label = QLabel('Apellidos: ')
        apellidos_label.setFixedWidth(60)
        self.Apellidos_input = QLineEdit()
        edad_label = QLabel('Edad: ')
        edad_label.setFixedWidth(60)
        self.edad_input = QLineEdit()
        correo_label = QLabel('Correo: ')
        correo_label.setFixedWidth(60)
        self.correo_input = QLineEdit()
        direccion_label = QLabel('Dirección: ')
        direccion_label.setFixedWidth(60)
        self.direccion_input = QLineEdit()
        telefono_label = QLabel('Telefono')
        telefono_label.setFixedWidth(60)
        self.telefono_input=QLineEdit()

        enviar_boton = QPushButton("Enviar")

        vertical_layout_main = QVBoxLayout()
        h_layout_1 = QHBoxLayout()
        h_layout_2 = QHBoxLayout()
        h_layout_3 = QHBoxLayout()

        h_layout_1.addWidget(nombres_label)
        h_layout_1.addWidget(self.nombres_input)
        h_layout_1.addWidget(correo_label)
        h_layout_1.addWidget(self.correo_input)

        h_layout_2.addWidget(apellidos_label)
        h_layout_2.addWidget(self.Apellidos_input)
        h_layout_2.addWidget(direccion_label)
        h_layout_2.addWidget(self.direccion_input)

        h_layout_3.addWidget(edad_label)
        h_layout_3.addWidget(self.edad_input)
        h_layout_3.addWidget(telefono_label)
        h_layout_3.addWidget(self.telefono_input)

        vertical_layout_main.addWidget(mensaje_principal)
        vertical_layout_main.addLayout(h_layout_1)
        vertical_layout_main.addLayout(h_layout_2)
        vertical_layout_main.addLayout(h_layout_3)
        vertical_layout_main.addWidget(enviar_boton)

        self.setLayout(vertical_layout_main)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())



