
from PyQt5.QtWidgets import QDockWidget, QColorDialog, QPushButton, QVBoxLayout, QWidget

class ColorPicker(QDockWidget):
    def __init__(self, parent=None):
        super().__init__("Color Picker", parent)
        self.init_ui()
        
    def init_ui(self):
        container = QWidget()
        layout = QVBoxLayout(container)
        
        # Color picker button
        self.color_button = QPushButton("Select Color")
        self.color_button.clicked.connect(self.show_color_dialog)
        layout.addWidget(self.color_button)
        
        self.setWidget(container)
        
    def show_color_dialog(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.parent().canvas.pen_color = color