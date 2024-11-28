from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
from editor.canvas import Canvas
from editor.toolbar import ToolBar
from editor.color_picker import ColorPicker
import sys

class SpriteEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sprite Editor")
        self.setGeometry(100, 100, 800, 600)
        
        # Initialize UI components
        self.canvas = Canvas(self)
        self.toolbar = ToolBar(self)
        self.color_picker = ColorPicker(self)
        
        # Set up layout
        self.setCentralWidget(self.canvas)
        self.addToolBar(self.toolbar)
        self.addDockWidget(Qt.RightDockWidgetArea, self.color_picker)

def main():
    app = QApplication(sys.argv)
    editor = SpriteEditor()
    editor.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()