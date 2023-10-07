import sys
from PyQt6.QtWidgets import (QApplication,QStatusBar,QLabel,QStatusBar, QMainWindow, QPushButton,
                             QDockWidget,QTabWidget,QWidget,QHBoxLayout,QVBoxLayout,
                             QListWidget)
from PyQt6.QtGui import (QPixmap)

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
        pixmap = QPixmap("PYQT6\Reproductor\images\sing.png")
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
        
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
            
        
        
        
        