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
        with open('Reproductor/estilos.css','r') as file:
            style = file.read()
        self.setStyleSheet(style)
    
    def inicializarUI(self):
        self.setGeometry(250,30,800,350)
        self.setWindowTitle("Reproductor de musica")
        self.setWindowIcon(QIcon('Reproductor/images/iconn.ico'))
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
        pixmap = QPixmap("Reproductor/images/song_image.png").scaled(512, 512)
        song_image.setPixmap(pixmap)
        song_image.setScaledContents(True)
        
        button_repeat = QPushButton()
        button_repeat.setObjectName("button_repeat")
        button_before = QPushButton()
        button_before.setObjectName("button_before")
        button_play = QPushButton()
        button_play.setObjectName("button_play")
        button_next = QPushButton()
        button_next.setObjectName("button_next")
        button_random = QPushButton()
        button_random.setObjectName("button_random")
        button_repeat.setFixedSize(40,40)
        button_before.setFixedSize(40,40)
        button_play.setFixedSize(50,50)
        button_next.setFixedSize(40,40)
        button_random.setFixedSize(40,40)

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
        icon = QIcon("Reproductor/images/mp3.ico")
        for archivo in os.listdir(selected_folder):
            ruta_archivo = os.path.join(selected_folder,archivo)
            if ruta_archivo.endswith(".mp3"):
                item = QListWidgetItem(archivo)
                item.setIcon(icon)
                self.songs_list.addItem(item)
                
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
<<<<<<< HEAD
    sys.exit(app.exec())
=======
    sys.exit(app.exec())
            
>>>>>>> 397d6a5 (Estilos reproductor)
