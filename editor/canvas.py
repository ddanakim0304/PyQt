
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QImage, QPen

class Canvas(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.image = QImage(32, 32, QImage.Format_ARGB32)
        self.image.fill(Qt.transparent)
        self.last_point = None
        self.drawing = False
        self.pen_color = Qt.black
        self.pen_size = 1
        
    def paintEvent(self, event):
        painter = QPainter(self)
        scaled_image = self.image.scaled(self.size(), Qt.KeepAspectRatio)
        painter.drawImage(0, 0, scaled_image)
        
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.last_point = self.convert_to_image_coords(event.pos())
            self.draw_point(self.last_point)
            
    def mouseMoveEvent(self, event):
        if self.drawing:
            current_point = self.convert_to_image_coords(event.pos())
            self.draw_line(self.last_point, current_point)
            self.last_point = current_point
            
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = False
            
    def convert_to_image_coords(self, pos):
        widget_size = self.size()
        image_size = self.image.size()
        x = int(pos.x() * image_size.width() / widget_size.width())
        y = int(pos.y() * image_size.height() / widget_size.height())
        return QPoint(x, y)
        
    def draw_point(self, point):
        painter = QPainter(self.image)
        painter.setPen(QPen(self.pen_color, self.pen_size))
        painter.drawPoint(point)
        self.update()
        
    def draw_line(self, start, end):
        painter = QPainter(self.image)
        painter.setPen(QPen(self.pen_color, self.pen_size))
        painter.drawLine(start, end)
        self.update()

    def clear_canvas(self):
        self.image.fill(Qt.transparent)
        self.update()