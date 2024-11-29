from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QImage, QPen

class Canvas(QWidget):
    MAX_HISTORY = 20

    def __init__(self, parent=None):
        super().__init__(parent)
        self.image = QImage(60, 60, QImage.Format_ARGB32)
        self.image.fill(Qt.transparent)
        self.last_point = None
        self.drawing = False
        self.pen_color = Qt.black
        self.pen_size = 1
        self.composition_mode = QPainter.CompositionMode_SourceOver

        # Add undo/redo stacks
        self.undo_stack = []
        self.redo_stack = []
        self.save_state()  # Save initial state

    def save_state(self):
        self.undo_stack.append(self.image.copy())
        self.redo_stack.clear()
        
        # Trim undo stack if exceeds limit
        if len(self.undo_stack) > self.MAX_HISTORY:
            self.undo_stack.pop(0)  # Remove oldest state
            
        # Enable/disable undo/redo buttons
        if hasattr(self.parent(), 'toolbar'):
            self.parent().toolbar.undo_action.setEnabled(True)
            self.parent().toolbar.redo_action.setEnabled(False)

    def undo(self):
        if len(self.undo_stack) > 1:
            self.redo_stack.append(self.undo_stack.pop())
            self.image = self.undo_stack[-1].copy()
            self.update()
            # Update button states
            self.parent().toolbar.undo_action.setEnabled(len(self.undo_stack) > 1)
            self.parent().toolbar.redo_action.setEnabled(True)

    def redo(self):
        if self.redo_stack:
            self.undo_stack.append(self.redo_stack.pop())
            self.image = self.undo_stack[-1].copy()
            self.update()
            # Update button states
            self.parent().toolbar.undo_action.setEnabled(True)
            self.parent().toolbar.redo_action.setEnabled(bool(self.redo_stack))

    def paintEvent(self, event):
        painter = QPainter(self)
        # Fill widget background with white
        painter.fillRect(self.rect(), Qt.white)

        # Get the scaled image size for debugging
        scaled_image = self.image.scaled(self.size(), Qt.KeepAspectRatio)
        scaled_size = scaled_image.size()
        # Calculate centering position
        x = (self.width() - scaled_size.width()) // 2
        y = (self.height() - scaled_size.height()) // 2
        painter.drawImage(x, y, scaled_image)
        
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            point = self.convert_to_image_coords(event.pos())
            if point:
                self.drawing = True
                self.last_point = point
                self.draw_point(self.last_point)
            
    def mouseMoveEvent(self, event):
        if self.drawing:
            current_point = self.convert_to_image_coords(event.pos())
            if current_point and self.last_point:
                self.draw_line(self.last_point, current_point)
                self.last_point = current_point
                self.update()
            
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = False
            self.save_state()  # Save state after drawing
            
    def convert_to_image_coords(self, pos):
        widget_size = self.size()
        image_size = self.image.size()
        
        # Calculate scaled image size
        scaled_size = self.image.scaled(widget_size, Qt.KeepAspectRatio).size()
        
        # Calculate the offset where the image is drawn
        x_offset = (widget_size.width() - scaled_size.width()) // 2
        y_offset = (widget_size.height() - scaled_size.height()) // 2
        
        # Adjust for offset
        pos_x = pos.x() - x_offset
        pos_y = pos.y() - y_offset
        
        # Scale to image coordinates
        if pos_x < 0 or pos_y < 0 or pos_x >= scaled_size.width() or pos_y >= scaled_size.height():
            return None
            
        x = int(pos_x * image_size.width() / scaled_size.width())
        y = int(pos_y * image_size.height() / scaled_size.height())
        
        return QPoint(x, y)
        
    def draw_point(self, point):
        if point:
            painter = QPainter(self.image)
            painter.setCompositionMode(self.composition_mode)
            painter.setPen(QPen(self.pen_color, self.pen_size))
            painter.drawPoint(point)
        
    def draw_line(self, start, end):
        painter = QPainter(self.image)
        painter.setCompositionMode(self.composition_mode)
        painter.setPen(QPen(self.pen_color, self.pen_size))
        painter.drawLine(start, end)
        self.update()

    def clear_canvas(self):
        self.image.fill(Qt.transparent)
        self.update()