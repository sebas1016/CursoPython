import sys
import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import (QApplication,QMainWindow,QStatusBar, QWidget, QFileDialog,
                              QVBoxLayout,QTextEdit,QFontDialog, QColorDialog)
from PyQt6.QtCore import QStandardPaths
from PyQt6.QtGui import QAction,QKeySequence,QIcon,QTextCharFormat, QGuiApplication

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.inicializarUI()
        self.status_bar.setStyleSheet("background-color: white;")
    
    def inicializarUI(self):
        self.setGeometry(100,100,500,500)
        self.setWindowTitle("QMainWindow")
        self.setWindowIcon(QIcon('PYQT6\layouts\images\icon_form.ico'))
        self.generateWindow()
        self.show()
    
    def generateWindow(self):
        self.create_content()
        self.create_action()
        self.create_menu()
    
    def create_content(self):
        layaout = QVBoxLayout()
        self.editor_text = QTextEdit()
        layaout.addWidget(self.editor_text)
        layaout.setContentsMargins(30,30,30,30)
        cointainer = QWidget()
        cointainer.setLayout(layaout)
        self.setCentralWidget(cointainer)
    
    def create_action(self):
        self.open_action = QAction("Abrir",self)
        self.open_action.setShortcut(QKeySequence('Ctrl+O'))
        self.open_action.setStatusTip("Abrir archivos")
        self.open_action.triggered.connect(self.open)

        self.save_action = QAction("Guardar",self)
        self.save_action.setShortcut(QKeySequence('Ctrl+S'))
        self.save_action.setStatusTip("Guardar Archivos")
        self.save_action.triggered.connect(self.save) 

        self.export_action = QAction("Exportar",self)
        self.export_action.setShortcut(QKeySequence('Ctrl+E'))
        self.export_action.setStatusTip("Guardar Archivos")
        self.export_action.triggered.connect(self.export)

        self.undo_action = QAction("Deshacer",self)
        self.undo_action.setShortcut(QKeySequence('Ctrl+Z'))
        self.undo_action.setStatusTip("Deshacer Cambio")
        self.undo_action.triggered.connect(self.editor_text.undo)

        self.redo_action = QAction("redo",self)
        self.redo_action.setShortcut(QKeySequence('Ctrl+Y'))
        self.redo_action.setStatusTip("Rehacer Cambio")
        self.redo_action.triggered.connect(self.editor_text.redo)

        self.font_action = QAction("Fuente",self)
        self.font_action.setShortcut(QKeySequence('Ctrl+F'))
        self.font_action.setStatusTip("Fuente")
        self.font_action.triggered.connect(self.set_font)

        self.color_action = QAction("Color",self)
        self.color_action.setShortcut(QKeySequence("Ctrl+K"))
        self.color_action.setStatusTip("Asignar Color")
        self.color_action.triggered.connect(self.set_color)

    def create_menu(self):
        menu_archivo = self.menuBar().addMenu("Archivo")
        menu_archivo.addAction(self.open_action)
        menu_archivo.addAction(self.save_action)
        menu_archivo.addAction(self.export_action)
        
        menu_editar = self.menuBar().addMenu("Editar")
        menu_editar.addAction(self.font_action)
        menu_editar.addAction(self.color_action)
        menu_editar.addAction(self.undo_action)
        menu_editar.addAction(self.redo_action)
    
    def open(self):
        options = (QFileDialog.Option.DontUseNativeDialog)
        initial_dir = QStandardPaths.writableLocation(QStandardPaths.StandardLocation.DesktopLocation)
        file_types = "Text Files(*.txt);;Imagenes (*.png);; All files (*);; HTML Files (*.html)"
        self.file , _ = QFileDialog.getOpenFileName(self,"Open File",initial_dir,file_types)
        
        with open(self.file, 'r') as file:
            self.setWindowTitle(f"QMainWindow - {self.file}")
            self.editor_text.setText(file.read())
        #Mostrar Texto
        
    def save(self):
        initial_dir = QStandardPaths.writableLocation(QStandardPaths.StandardLocation.DesktopLocation)
        file_types = "Text Files(*.txt);;Imagenes (*png);; All files (*);; HTML Files (*.html)"
        file_name , _ = QFileDialog.getSaveFileName(self,"Save File",initial_dir,file_types)
        if file_name.endswith(".txt"):
            try:
                with open(file_name, 'w') as file:
                    file.write(f"{self.editor_text.toPlainText()}\n")
                file.close()
            except (FileNotFoundError) as e:
                print(f"Error fatal perro: {e}")
        elif file_name.endswith(".html"):
            try:
                with open(file_name, 'w') as file:
                    file.write(f"{self.editor_text.toHtml()}\n")
                file.close()
            except (FileNotFoundError) as e:
                print(f"Error fatal perro: {e}")
    def set_font(self):
        selected_text_cursor = self.editor_text.textCursor() 
        fonti = QFontDialog()
        fonti.setWindowIcon(QIcon('PYQT6\layouts\images\icon_form.ico'))
        font , ok = fonti.getFont(self.editor_text.currentFont(),self)

        if ok:
            if selected_text_cursor.hasSelection():
                format = self.editor_text.currentCharFormat()
                format.setFont(font)
                selected_text_cursor.mergeCharFormat(format)
            else:
                self.editor_text.setCurrentFont(font)

    def export(self):
        initial_dir = QStandardPaths.writableLocation(QStandardPaths.StandardLocation.DesktopLocation)
        screen = QGuiApplication.primaryScreen()
        file_types = "TImagenes (*png)"
        pixmap = screen.grabWindow(self.editor_text.winId())

        file_name, _ = QFileDialog.getSaveFileName(self, "guardar archivo", initial_dir,file_types)
        if file_name:
            pixmap.save(file_name)

    def set_color(self):
        select_text_cursor = self.editor_text.textCursor()
        colors = QColorDialog()
        colors.setWindowTitle('Paleta')
        colors.setWindowIcon(QIcon('PYQT6\layouts\images\paleta.ico'))
        color = colors.getColor(self.editor_text.textColor(),self)

        if color.isValid:
            if select_text_cursor.hasSelection():
                format = QTextCharFormat()
                format.setForeground(color)
                select_text_cursor.mergeCharFormat(format)
            else:
                self.editor_text.setTextColor(color)
    
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())