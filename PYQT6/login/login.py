import sys
import typing
from registro import RegistrarUsuarioView
from main import MainWindow
from PyQt6 import QtCore
from PyQt6.QtWidgets import (QApplication, QLabel, QWidget, QLineEdit, QPushButton,
                              QMessageBox, QCheckBox)
from PyQt6.QtGui import QFont, QPixmap

class Login(QWidget):
    
    def __init__(self):
        super().__init__()
        self.inicializar_ui()
    
    def inicializar_ui(self):
        self.setGeometry(150, 150, 350, 300)
        self.setWindowTitle('Login')
        self.generar_formulario()
        self.show()
    
    def generar_formulario(self):
        self.is_logged = False
        user_label = QLabel(self)
        user_label.setText("Usuario: ")
        user_label.setFont(QFont('Arial', 10))
        user_label.move(20,54)

        self.user_input = QLineEdit(self)
        self.user_input.resize(250,24)
        self.user_input.move(90,54)
        
        password_label = QLabel(self)
        password_label.setText("Password: ")
        password_label.setFont(QFont('Arial', 10))
        password_label.move(20,86)

        self.password_input = QLineEdit(self)
        self.password_input.resize(250,24)
        self.password_input.move(90,86)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.chek_view_password = QCheckBox(self)
        self.chek_view_password.setText("Ver contraseña")
        self.chek_view_password.move(90, 110)
        self.chek_view_password.clicked.connect(self.show_password)

        login_button = QPushButton(self)
        login_button.setText("Login")
        login_button.resize(320, 34)
        login_button.move(20, 140)
        login_button.clicked.connect(self.login)

        register_button = QPushButton(self)
        register_button.setText("Register")
        register_button.resize(320, 34)
        register_button.move(20, 180)
        register_button.clicked.connect(self.register_user)

    def show_password(self,clicked):
        if clicked:
            self.password_input.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        

    def login(self):
        user = []
        user_path = 'usuarios.txt'

        try:
            with open(user_path, 'r') as f:
                for linea in f:
                    user.append(linea.strip("\n"))
            login_information = f"{self.user_input.text()},{self.password_input.text()}"

            if login_information in user:
                QMessageBox.information(self, 'Login exitoso',
                                        'Inicio de sesion exitoso',
                                        QMessageBox.StandardButton.Ok,
                                        QMessageBox.StandardButton.Ok)
                self.is_logged = True
                self.close()
                self.open_main_window()
            
            else:
                QMessageBox.warning(self, 'Error',
                                    'Usuario no registrado',
                                    QMessageBox.StandardButton.Close,
                                    QMessageBox.StandardButton.Close)
        except FileNotFoundError as e:
            QMessageBox.warning(self, 'Error',
                                f'Base de Datos no encontrada: {e}',
                                QMessageBox.StandardButton.Close,
                                QMessageBox.StandardButton.Close)
            
    def register_user(self):
        self.new_use_form = RegistrarUsuarioView()
        self.new_use_form.show()
    
    def open_main_window(self):
        self.main_window = MainWindow()
        self.main_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = Login()
    sys.exit(app.exec())
