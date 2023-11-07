import sys
import os
from PyQt6.QtWidgets import (QApplication,QStatusBar,QLabel,QStatusBar, QMainWindow, QPushButton,
                             QDockWidget,QTabWidget,QWidget,QHBoxLayout,QVBoxLayout,
                             QListWidget,QFileDialog,QListWidgetItem)
from PyQt6.QtMultimedia import (QMediaPlayer, QAudioOutput)
from PyQt6.QtCore import (Qt, QStandardPaths,QUrl,QModelIndex)
from PyQt6.QtGui import (QPixmap, QAction, QKeySequence,QIcon)


class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.current_music_folder = ""
        with open('Reproductor/estilos.css','r') as file:
            style = file.read()
        self.setStyleSheet(style)
        self.player = QMediaPlayer()
        self.playing_reproductor = True
        self.nexted_song = False
        self.inicializarUI()
        
    def inicializarUI(self):
        self.setGeometry(250,30,800,350)
        self.setWindowTitle("Reproductor de musica")
        self.setWindowIcon(QIcon('Reproductor/images/iconn.ico'))
        self.generateMainWindow()
        self.create_dock()
        self.create_action()
        self.create_menu()
        self.load_songs()
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
        
        self.button_repeat = QPushButton()
        self.button_repeat.setObjectName("button_repeat")
        self.button_before = QPushButton()
        self.button_before.setObjectName("button_before")
        self.button_play = QPushButton()
        self.button_play.setObjectName("button_play")
        self.button_play.clicked.connect(self.play_pause_song)
        self.button_next = QPushButton()
        self.button_next.setObjectName("button_next")
        self.button_next.clicked.connect(self.next_song)
        self.button_random = QPushButton()
        self.button_random.setObjectName("button_random")
        self.button_repeat.setFixedSize(40,40)
        self.button_before.setFixedSize(40,40)
        self.button_play.setFixedSize(50,50)
        self.button_next.setFixedSize(40,40)
        self.button_random.setFixedSize(40,40)

        button_h_box.addWidget(self.button_repeat)
        button_h_box.addWidget(self.button_before)
        button_h_box.addWidget(self.button_play)
        button_h_box.addWidget(self.button_next)
        button_h_box.addWidget(self.button_random)
        
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
        self.songs_list.itemSelectionChanged.connect(self.handle_song_selection)
        self.dock.setWidget(self.songs_list)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea,self.dock)
        
    def list_music(self):
        if self.listar_musica_action.isChecked():
            self.dock.show()
        else:
            self.dock.hide()
            
    def open_folder_music(self):
        self.songs_list.clear()
        initial_dir = QStandardPaths.writableLocation(QStandardPaths.StandardLocation.MusicLocation)
        self.current_music_folder = QFileDialog.getExistingDirectory(None, "Selecciona una carpeta", initial_dir)
        print(self.current_music_folder)
        icon = QIcon("Reproductor/images/mp3.ico")
        try:
            for archivo in os.listdir(self.current_music_folder):
                ruta_archivo = os.path.join(self.current_music_folder,archivo)
                if ruta_archivo.endswith(".mp3"):
                    item = QListWidgetItem(archivo)
                    item.setIcon(icon)
                    self.songs_list.addItem(item)
        except(FileNotFoundError) as e:
            print(f"No se encontro el archivo {e}")
            
    def load_songs(self):
        self.current_music_folder = QStandardPaths.writableLocation(QStandardPaths.StandardLocation.MusicLocation)
        print(self.current_music_folder)
        try:
            icon = QIcon("Reproductor/images/mp3.ico")
            for archivo in os.listdir(self.current_music_folder):
                ruta_archivo = os.path.join(self.current_music_folder,archivo)
                if ruta_archivo.endswith(".mp3"):
                    item = QListWidgetItem(archivo)
                    item.setIcon(icon)
                    self.songs_list.addItem(item)
                    
        except(FileNotFoundError) as e:
            print(f"No se encontro el archivo {e}") 
        
                       
    def create_player(self):
        if self.player:
            self.player.deleteLater()
        self.player = QMediaPlayer()
        self.audioOuput = QAudioOutput()
        self.player.setAudioOutput(self.audioOuput)
        self.player.mediaStatusChanged.connect(self.mediaStatusChange)
        self.audioOuput.setVolume(1.0)
        
    #SLOT HANDLE
    def play_pause_song(self):
        if self.playing_reproductor:
            self.button_play.setStyleSheet("image: url(Reproductor/images/pausa.png)")
            self.player.pause()
            self.playing_reproductor = False
        else:
            self.button_play.setStyleSheet("image: url(Reproductor/images/jugar.png)")
            self.player.play()
            self.playing_reproductor = True
    
    def next_song(self):
        #self.get_current_playing_index()
        selected_item_index = ""#self.get_current_playing_index()
        print(selected_item_index)
        if self.songs_list.count() > 0:
            self.next_index = selected_item_index+1
            if self.next_index == (self.songs_list.count()):
                self.next_index = 0
                print(self.next_index)
            print(self.next_index)
            selected_item = self.songs_list.item(self.next_index)
            song_name = selected_item.text()
            song_folder_path = os.path.join(self.current_music_folder, song_name)
            self.create_player()
            source = QUrl.fromLocalFile(song_folder_path)
            self.player.setSource(source)
            self.player.play()  
        else:
            posision = self.player.position()
            curren_index = self.songs_list.currentIndex()
            print("No hay canciones en la lista",posision,curren_index)   
                   
    def get_current_playing_index(self):
        #current_media_url = self.player.source().path()
        #print(current_media_url)
        #current_song_path = QUrl(current_media_url).toLocalFile()
        #print(current_song_path)
        selected_item = self.songs_list.currentItem()
        song_name = selected_item.data(0)
        song_folder_path = os.path.join(self.current_music_folder, song_name)
        current_song_path = QUrl.fromLocalFile(song_folder_path)
        for index in range(self.songs_list.count()):
            item = self.songs_list.item(index)
            song_path = os.path.join(self.current_music_folder, item.text())
            if song_path == current_song_path:
                return index

        return -1  # Retorna -1 si no se encuentra la canción en la lista        
    def mediaStatusChange(self,status):
        print('Status: ',status)
        if status == QMediaPlayer.MediaStatus.LoadedMedia:
            self.player.play()
            
            
    def handle_song_selection(self):
        selected_item = self.songs_list.currentItem()
        if selected_item:
            song_name = selected_item.data(0)
            song_folder_path = os.path.join(self.current_music_folder, song_name)
            self.create_player()
            source = QUrl.fromLocalFile(song_folder_path)
            self.player.setSource(source)
            
                
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
