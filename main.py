from PyQt5.QtWidgets import QApplication, QMainWindow, QShortcut
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeySequence
from editor.canvas import Canvas
from editor.toolbar import ToolBar
from editor.color_picker import ColorPicker
from editor.menu import MenuBar
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
        self.menu_bar = MenuBar(self)
        
        # Set up layout
        self.setCentralWidget(self.canvas)
        self.addToolBar(self.toolbar)
        self.addDockWidget(Qt.RightDockWidgetArea, self.color_picker)

        # Shortcuts
        QShortcut(QKeySequence.Undo, self).activated.connect(self.canvas.undo)
        QShortcut(QKeySequence.Redo, self).activated.connect(self.canvas.redo)

def main():
    app = QApplication(sys.argv)
    editor = SpriteEditor()
    editor.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()