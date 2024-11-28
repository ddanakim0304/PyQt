from PyQt5.QtCore import QFile, QIODevice
from PyQt5.QtGui import QImage

def save_sprite(image, filename):
    """Save the sprite as a PNG file"""
    return image.save(filename, "PNG")

def load_sprite(filename):
    """Load a sprite from a PNG file"""
    image = QImage()
    if image.load(filename):
        return image
    return None