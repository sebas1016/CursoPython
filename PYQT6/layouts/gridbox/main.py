import sys
import typing
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QWidget, QTextEdit, QPushButton, QGridLayout)
from PyQt6.QtGui import QKeySequence
import operator

operation = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,
    '^' : operator.pow
}

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()
        self.primer_valor = ''
        self.segundo_valor = ''
        self.operador = ''
        self.bandera = '1'
        self.after_equal = False
        self.after_operador = False
        with open("layouts/gridbox/style.css", "r") as file:
            style = file.read()
        
        self.setStyleSheet(style)

    def inicializarUI(self):
        self.setGeometry(100,100,600,400)
        self.setWindowTitle("Calculadora")
        self.generar_interfaz()
        self.show()
    
    def generar_interfaz(self):
        self.pantalla = QTextEdit()
        self.pantalla.setObjectName("pantalla")
        self.pantalla.setDisabled(True)
        boton_1 = QPushButton("1")
        boton_2 = QPushButton("2")
        boton_3 = QPushButton("3")
        boton_4 = QPushButton("4")
        boton_5 = QPushButton("5")
        boton_6 = QPushButton("6")
        boton_7 = QPushButton("7")
        boton_8 = QPushButton("8")
        boton_9 = QPushButton("9")
        boton_0 = QPushButton("0")
        boton_00 = QPushButton("00")
        boton_punto = QPushButton(".")

        boton_1.clicked.connect(self.ingresar_datos)
        boton_1.setShortcut(QKeySequence(Qt.Key.Key_1))
        boton_2.clicked.connect(self.ingresar_datos)
        boton_2.setShortcut(QKeySequence(Qt.Key.Key_2))
        boton_3.clicked.connect(self.ingresar_datos)
        boton_3.setShortcut(QKeySequence(Qt.Key.Key_3))
        boton_4.clicked.connect(self.ingresar_datos)
        boton_4.setShortcut(QKeySequence(Qt.Key.Key_4))
        boton_5.clicked.connect(self.ingresar_datos)
        boton_5.setShortcut(QKeySequence(Qt.Key.Key_5))
        boton_6.clicked.connect(self.ingresar_datos)
        boton_6.setShortcut(QKeySequence(Qt.Key.Key_6))
        boton_7.clicked.connect(self.ingresar_datos)
        boton_7.setShortcut(QKeySequence(Qt.Key.Key_7))
        boton_8.clicked.connect(self.ingresar_datos)
        boton_8.setShortcut(QKeySequence(Qt.Key.Key_8))
        boton_9.clicked.connect(self.ingresar_datos)
        boton_9.setShortcut(QKeySequence(Qt.Key.Key_9))
        boton_0.clicked.connect(self.ingresar_datos)
        boton_0.setShortcut(QKeySequence(Qt.Key.Key_0))
        boton_00.clicked.connect(self.ingresar_datos)
        boton_punto.clicked.connect(self.ingresar_datos)
        boton_punto.setShortcut(QKeySequence('.'))

        boton_suma = QPushButton("+")
        boton_suma.setShortcut(QKeySequence('+'))
        boton_resta = QPushButton("-")
        boton_resta.setShortcut(QKeySequence('-'))
        boton_multiplicacion = QPushButton("*")
        boton_multiplicacion.setShortcut(QKeySequence('*'))
        boton_division = QPushButton("/")
        boton_division.setShortcut(QKeySequence(Qt.Key.Key_Slash))

        boton_suma.clicked.connect(self.insertar_operador)
        boton_resta.clicked.connect(self.insertar_operador)
        boton_multiplicacion.clicked.connect(self.insertar_operador)
        boton_division.clicked.connect(self.insertar_operador)

        boton_igual = QPushButton("=")
        boton_igual.setObjectName("boton_igual")
        boton_igual.setShortcut(QKeySequence(Qt.Key.Key_Return))
        boton_ce = QPushButton("CE")
        boton_ce.setShortcut(QKeySequence(Qt.Key.Key_Delete))
        boton_borrar = QPushButton("<-")
        boton_borrar.setShortcut(QKeySequence(Qt.Key.Key_Backspace))

        boton_igual.clicked.connect(self.calcular_operacion)
        boton_ce.clicked.connect(self.borrar_todo)
        boton_borrar.clicked.connect(self.borrar_parcial)

        self.main_grid = QGridLayout()
        self.main_grid.addWidget(self.pantalla,0,0,2,4)

        self.main_grid.addWidget(boton_ce,2,0,1,2)
        self.main_grid.addWidget(boton_borrar,2,2)
        self.main_grid.addWidget(boton_suma,2,3)

        self.main_grid.addWidget(boton_7,3,0)
        self.main_grid.addWidget(boton_8,3,1)
        self.main_grid.addWidget(boton_9,3,2)
        self.main_grid.addWidget(boton_division,3,3)
        
        self.main_grid.addWidget(boton_4,4,0)
        self.main_grid.addWidget(boton_5,4,1)
        self.main_grid.addWidget(boton_6,4,2)
        self.main_grid.addWidget(boton_multiplicacion,4,3)

        self.main_grid.addWidget(boton_1,5,0)
        self.main_grid.addWidget(boton_2,5,1)
        self.main_grid.addWidget(boton_3,5,2)
        self.main_grid.addWidget(boton_resta,5,3)

        self.main_grid.addWidget(boton_0,6,0)
        self.main_grid.addWidget(boton_00,6,1)
        self.main_grid.addWidget(boton_punto,6,2)
        self.main_grid.addWidget(boton_igual,6,3)

        self.setLayout(self.main_grid)

    def ingresar_datos(self):
        boton_text = self.sender().text()
        if self.after_equal:
            self.primer_valor=''
            self.pantalla.setText(self.primer_valor)
            self.after_equal = False
            self.bandera = '1'

        if self.bandera == '1':
            self.primer_valor += boton_text
            self.pantalla.setText(self.primer_valor)
        else:
            self.segundo_valor += boton_text
            self.pantalla.setText(self.pantalla.toPlainText() + self.segundo_valor)

    def insertar_operador(self):
        boton_text = self.sender().text()
        self.operador = boton_text
        self.bandera = '2'

        if self.after_operador:
            self.calcular_operacion()
            self.pantalla.setText(self.primer_valor+' '+self.operador+' ')
            self.after_operador= False
        else:
            self.pantalla.setText(self.pantalla.toPlainText()+ ' '+self.operador+'')
        self.after_operador=True
        self.after_equal = False
    
    def borrar_todo(self):
        self.primer_valor = ''
        self.segundo_valor = ''
        self.operador = ''
        self.bandera = '1'
        self.after_equal = False
        self.after_operador = False
        self.pantalla.setText("")

    def borrar_parcial(self):
        if self.after_equal:
            self.borrar_todo()
        elif self.bandera == '1':
            self.primer_valor = self.primer_valor[:-1]
            self.pantalla.setText(self.primer_valor)
        else:
            self.segundo_valor=self.segundo_valor[:-1]
            self.pantalla.setText(self.segundo_valor)    

    def calcular_operacion(self):
        if (self.primer_valor != "" and self.segundo_valor != ""):
            resultado = str(operation[self.operador](float(self.primer_valor),float(self.segundo_valor)))
            self.pantalla.setText(resultado)
            self.primer_valor = resultado
            self.segundo_valor = ''
            self.after_equal = True
            self.after_operador = False
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())