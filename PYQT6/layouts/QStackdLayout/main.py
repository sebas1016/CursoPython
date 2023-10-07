import sys
import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import(QApplication,QWidget,QLabel,QLineEdit,QTextEdit,QPushButton,QStackedLayout,QFormLayout,QVBoxLayout,QHBoxLayout,QDateEdit,QMessageBox, QComboBox)
from PyQt6.QtCore import Qt,QDate
from PyQt6.QtGui import QPixmap,QFont

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()
    
    def inicializarUI(self):
        self.setFixedSize(600,600)
        self.setWindowTitle("QStackedLayout")
        self.generate_window()
        self.show()

    def generate_window(self):
        button_1 = QPushButton("Ventana 1")
        button_1.clicked.connect(self.change_window)
        button_2 = QPushButton("Ventana 2")
        button_2.clicked.connect(self.change_window)
        button_3 = QPushButton("Ventana 3")
        button_3.clicked.connect(self.change_window)

        buttons_group = QHBoxLayout()
        buttons_group.addWidget(button_1)
        buttons_group.addWidget(button_2)
        buttons_group.addWidget(button_3)

        #pagina 1
        tittle = QLabel("Mapa")
        tittle.setFont(QFont('Arial',18))
        tittle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        image_map = QLabel()
        pixmap = QPixmap("PYQT6\layouts\images\colombia_mapa.png")
        image_map.setPixmap(pixmap)
        #Obtener el tamaño de la ventana
        window_size = self.size()
        image_map.setMaximumSize(window_size)
        image_map.setScaledContents(True)

        page1_layout = QVBoxLayout()
        page1_layout.addWidget(tittle)
        page1_layout.addWidget(image_map)

        container_1 = QWidget()
        container_1.setLayout(page1_layout)

        #Pagina 2
        tittle2 = QLabel("Solicitud de ingreso")
        tittle2.setFont(QFont('Arial',18))
        tittle2.setAlignment(Qt.AlignmentFlag.AlignCenter)

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

        form_2 = QFormLayout()
        form_2.addRow(tittle2)
        form_2.addRow("Nombre: ",primer_h_box)
        form_2.addRow("Genero: ",self.genero_select)
        form_2.addRow("Fecha: ",self.fecha_nacimiento)
        form_2.addRow("Telefono: ",self.telefono_edit)
        form_2.addRow(submit_button)

        cointainer_2 = QWidget()
        cointainer_2.setLayout(form_2)

        #Pagina 2

        tittle3 = QLabel("Observaciones")
        tittle3.setFont(QFont('Arial',18))
        tittle3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.observations = QTextEdit()
        form_3 = QFormLayout()
        form_3.addRow(tittle3)
        form_3.addRow("Observaciones",self.observations)

        cointainer_3 = QWidget()
        cointainer_3.setLayout(form_3)

        self.stacked_layout = QStackedLayout()
        self.stacked_layout.addWidget(container_1)
        self.stacked_layout.addWidget(cointainer_2)
        self.stacked_layout.addWidget(cointainer_3)

        main_layout = QVBoxLayout()
        main_layout.addLayout(buttons_group)
        main_layout.addLayout(self.stacked_layout)
        self.setLayout(main_layout)

    def change_window(self):
        button = self.sender()

        if button.text().lower() == 'ventana 1':
            self.stacked_layout.setCurrentIndex(0)
        elif button.text().lower() == 'ventana 2':
            self.stacked_layout.setCurrentIndex(1)
        else: 
            self.stacked_layout.setCurrentIndex(2)    

    def mostrar_informacion(self):
        QMessageBox.information(self,'Información',
                                f"Nombre: {self.nombre_edit.text()} {self.apellido_edit.text()} \n \
                                  Genero: {self.genero_select.currentText()} \n \
                                  Fecha: {self.fecha_nacimiento.text()} \n \
                                  Telefono: {self.telefono_edit.text()}",
                                  QMessageBox.StandardButton.Ok,
                                  QMessageBox.StandardButton.Ok)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())