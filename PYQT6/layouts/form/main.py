import sys
import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QDateEdit, QLineEdit,QComboBox,QFormLayout,QHBoxLayout,QMessageBox, )
from PyQt6.QtGui import QFont,QIcon
from PyQt6.QtCore import Qt, QDate

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self. inicializarUI()
    
    def inicializarUI(self):
        icon_path = 'layouts\images\icon_form.ico'
        self.setGeometry(100,100,450,200)
        self.setWindowTitle('FormLayout')
        self.setWindowIcon(QIcon(icon_path))
        self.crear_formulario()
        self.show()
    
    def crear_formulario(self):
        titulo = QLabel("Solicitud de ingreso")
        titulo.setFont(QFont('Arial',18))
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.nombre_edit = QLineEdit()
        self.nombre_edit.setPlaceholderText("Nombre")
        self.apellido_edit = QLineEdit()
        self.apellido_edit.setPlaceholderText("Apellido")

        self.genero_select = QComboBox()
        self.genero_select.addItems(["Masculino","Femenino","Otro"])

        self.fecha_nacimiento = QDateEdit()
        self.fecha_nacimiento.setDisplayFormat("yyyy-MM-dd")
        self.fecha_nacimiento.setMaximumDate(QDate.currentDate())
        self.fecha_nacimiento.setCalendarPopup(True)
        self.fecha_nacimiento.setDate(QDate.currentDate())

        self.telefono_edit = QLineEdit()
        self.telefono_edit.setPlaceholderText("604 - 44433")

        submit_button = QPushButton("Enviar")
        submit_button.clicked.connect(self.mostrar_informacion)

        primer_h_box = QHBoxLayout()
        primer_h_box.addWidget(self.nombre_edit)
        primer_h_box.addWidget(self.apellido_edit)

        main_form = QFormLayout()

        main_form.addRow(titulo)
        main_form.addRow("Nombre: ",primer_h_box)
        main_form.addRow("Genero: ",self.genero_select)
        main_form.addRow("Fecha: ",self.fecha_nacimiento)
        main_form.addRow("Telefono: ",self.telefono_edit)
        main_form.addRow(submit_button)

        self.setLayout(main_form)

    def mostrar_informacion(self):
        QMessageBox.information(self,'Información',
                                f"Nombre: {self.nombre_edit.text()} {self.apellido_edit.text()} \n \
                                  Genero: {self.genero_select.currentText()} \n \
                                  Fecha: {self.fecha_nacimiento.text()} \n \
                                  Telefono: {self.telefono_edit.text()}",
                                  QMessageBox.StandardButton.Ok,
                                  QMessageBox.StandardButton.Ok)
        
        self.nombre_edit.setText("")
        self.fecha_nacimiento.setDate(QDate.currentDate())
        self.apellido_edit.setText("")
        self.telefono_edit.setText("")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
        