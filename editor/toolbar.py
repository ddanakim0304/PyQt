from PyQt5.QtWidgets import QToolBar, QAction
from PyQt5.QtCore import Qt

class ToolBar(QToolBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_tools()
        
    def init_tools(self):
        # Pen tool
        pen_action = QAction("Pen", self)
        pen_action.setCheckable(True)
        pen_action.setChecked(True)
        self.addAction(pen_action)
        
        # Eraser tool
        eraser_action = QAction("Eraser", self)
        eraser_action.setCheckable(True)
        self.addAction(eraser_action)
        
        # Add separator
        self.addSeparator()
        
        # Clear canvas action
        clear_action = QAction("Clear", self)
        clear_action.triggered.connect(self.parent().canvas.clear_canvas)
        self.addAction(clear_action)