import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import (QDialog,QLabel, QPushButton,QLineEdit, QMessageBox, QWidget, )
from PyQt6.QtGui import QFont
import PyQt6.sip

class RegistrarUsuarioView(QDialog):

    def __init__(self):
        super().__init__()
        self.setModal(True)
        self.generar_formulario()

    def generar_formulario(self):
        self.setGeometry(100, 100, 350, 250)
        self.setWindowTitle("Registration Window")

        user_label = QLabel(self)
        user_label.setText("Usuario:")
        user_label.setFont(QFont('Arial',10))
        user_label.move(20,44)

        self.user_input = QLineEdit(self)
        self.user_input.resize(250,24)
        self.user_input.move(90,40)

        password_1_label = QLabel(self)
        password_1_label.setText("Password:")
        password_1_label.setFont(QFont('Arial',10))
        password_1_label.move(20,74)

        self.password_1_input=QLineEdit(self)
        self.password_1_input.resize(250,24)
        self.password_1_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_1_input.move(90,70)

        password_label = QLabel(self)
        password_label.setText("Validation Password")
        password_label.setFont(QFont('Arial',10))
        password_label.move(90,104)

        self.password_input = QLineEdit(self)
        self.password_input.resize(250,24)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.move(90,100)

        create_button = QPushButton(self)
        create_button.setText("Register")
        create_button.resize(150,32)
        create_button.move(20,170)
        create_button.clicked.connect(self.create_user)

        cancel_button = QPushButton(self)
        cancel_button.setText("Cancel")
        cancel_button.resize(150,32)
        cancel_button.move(170,170)
        cancel_button.clicked.connect(self.cancel_register)

    def cancel_register(self):
        self.close()
    
    def create_user(self):
        user_path = 'usuarios.txt'
        user = self.user_input.text()
        password1 = self.password_1_input.text()
        password = self.password_input.text()

        if password1 == '' or password == '' or user == '':
            QMessageBox.warning(self, 'Error:', 
                                'Ingrese datos  validos', 
                                QMessageBox.StandardButton.Close,
                                QMessageBox.StandardButton.Close)
        elif password1 != password:
            QMessageBox.warning(self, 'Error',
                                'Las contraseñas no coinciden',
                                QMessageBox.StandardButton.Close,
                                QMessageBox.StandardButton.Close)
        else:
            try:
                with open(user_path, 'a+') as f:
                    f.write(f"{user},{password}\n")
                QMessageBox.information(self, 'Registro Exitoso',
                                        'Usuario creado exitosamente',
                                        QMessageBox.StandardButton.Ok,
                                        QMessageBox.StandardButton.Ok)
                self.close()
                
            except FileNotFoundError as e:
                QMessageBox.warning(self, 'Error',
                                    f'La base de datos de usuario no existe:{e}',
                                    QMessageBox.StandardButton.Close,
                                    QMessageBox.StandardButton.Close)




    