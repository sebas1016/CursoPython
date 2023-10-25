import sys
import os
from PyQt6.QtWidgets import (QApplication,QStatusBar,QLabel,QStatusBar, QMainWindow, QPushButton,
                             QDockWidget,QTabWidget,QWidget,QHBoxLayout,QVBoxLayout,
                             QListWidget,QFileDialog,QListWidgetItem)
from PyQt6.QtCore import (Qt, QStandardPaths)
from PyQt6.QtGui import (QPixmap, QAction, QKeySequence,QIcon)

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.inicializarUI()
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
    
    def inicializarUI(self):
        self.setGeometry(100,100,800,500)
        self.setWindowTitle("Reproductor de musica")
        self.generateMainWindow()
        self.create_dock()
        self.create_action()
        self.create_menu()
        self.show()
    
    def generateMainWindow(self):
        tab_bar = QTabWidget(self)
        self.reproductor_cointainer = QWidget()
        self.settings_cointainer = QWidget()
        tab_bar.addTab(self.reproductor_cointainer, "Reproductor")
        tab_bar.addTab(self.settings_cointainer, "Configuraciones")
        
        self.generate_reproductor_tab()
        #self.generate_settings_tab()
        
        tab_h_box = QHBoxLayout()
        tab_h_box.addWidget(tab_bar)
        
        main_cointainer = QWidget()
        main_cointainer.setLayout(tab_h_box)
        self.setCentralWidget(main_cointainer)
    
    def generate_reproductor_tab(self):
        main_V_box = QVBoxLayout()
        button_h_box = QHBoxLayout()
        buttons_cointainer = QWidget()
        
        song_image = QLabel()
        pixmap = QPixmap("PYQT6/Reproductor/images/song_image.png")
        song_image.setPixmap(pixmap)
        song_image.setScaledContents(True)
        
        button_repeat = QPushButton("Repeat")
        button_before = QPushButton("Before")
        button_play = QPushButton("Play")
        button_next = QPushButton("next")
        button_random = QPushButton("Random")
        
        button_h_box.addWidget(button_repeat)
        button_h_box.addWidget(button_before)
        button_h_box.addWidget(button_play)
        button_h_box.addWidget(button_next)
        button_h_box.addWidget(button_random)
        
        buttons_cointainer.setLayout(button_h_box)
        main_V_box.addWidget(song_image)
        main_V_box.addWidget(buttons_cointainer)
        self.reproductor_cointainer.setLayout(main_V_box)
    
    def create_action(self):
        self.listar_musica_action = QAction("Listar Musica", self,checkable = True)
        self.listar_musica_action.setShortcut(QKeySequence("Ctrl+L")) 
        self.listar_musica_action.triggered.connect(self.list_music)
        self.listar_musica_action.setChecked(True)
        self.listar_musica_action.setStatusTip("Muestra tu carpeta de musica")
            
        self.open_folder_music_action = QAction("Abrir Carpeta",self)
        self.open_folder_music_action.setShortcut(QKeySequence('Ctrl+O'))
        self.open_folder_music_action.setStatusTip("Abre tu carpeta de musica")
        self.open_folder_music_action.triggered.connect(self.open_folder_music)
        
    def create_menu(self):
        self.menuBar()
        menu_file = self.menuBar().addMenu("File")
        menu_file.addAction(self.open_folder_music_action)
        menu_view = self.menuBar().addMenu("View")
        menu_view.addAction(self.listar_musica_action)
    
    def create_dock(self):
        self.songs_list = QListWidget()
        self.dock = QDockWidget()
        self.dock.setWindowTitle("Lista de canciones")
        self.dock.setAllowedAreas(Qt.DockWidgetArea.LeftDockWidgetArea | Qt.DockWidgetArea.RightDockWidgetArea)
        self.dock.setWidget(self.songs_list)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea,self.dock)
        
    def list_music(self):
        if self.listar_musica_action.isChecked():
            self.dock.show()
        else:
            self.dock.hide()
            
    def open_folder_music(self):
        initial_dir = QStandardPaths.writableLocation(QStandardPaths.StandardLocation.MusicLocation)
        selected_folder = QFileDialog.getExistingDirectory(None, "Selecciona una carpeta", initial_dir)
        icon = QIcon("PYQT6\Reproductor\images\mp3.ico")
        for archivo in os.listdir(selected_folder):
            ruta_archivo = os.path.join(selected_folder,archivo)
            if ruta_archivo.endswith(".mp3"):
                item = QListWidgetItem(archivo)
                item.setIcon(icon)
                self.songs_list.addItem(item)
                
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())