from PyQt5.QtWidgets import QMenuBar, QAction, QFileDialog
from utils.file_handler import save_sprite, load_sprite

class MenuBar(QMenuBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_menus()
        
    def init_menus(self):
        # File Menu
        file_menu = self.addMenu("File")
        
        # Save Action
        save_action = QAction("Save", self)
        save_action.setShortcut("Ctrl+S")
        save_action.triggered.connect(self.save_sprite)
        file_menu.addAction(save_action)
        
        # Load Action
        load_action = QAction("Load", self)
        load_action.setShortcut("Ctrl+O")
        load_action.triggered.connect(self.load_sprite)
        file_menu.addAction(load_action)
        
    def save_sprite(self):
        filename, _ = QFileDialog.getSaveFileName(
            self,
            "Save Sprite",
            "",
            "PNG Files (*.png)"
        )
        if filename:
            save_sprite(self.parent().canvas.image, filename)
            
    def load_sprite(self):
        filename, _ = QFileDialog.getOpenFileName(
            self,
            "Load Sprite",
            "",
            "PNG Files (*.png)"
        )
        if filename:
            image = load_sprite(filename)
            if image:
                self.parent().canvas.image = image
                self.parent().canvas.update()