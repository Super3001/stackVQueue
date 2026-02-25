from PyQt6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QSplitter
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QFont
from src.data_model import DataManager
from src.widgets import StackWidget, QueueWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.data_manager = DataManager()
        self.drag_pos = None
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Stack & Queue 演示程序")
        self.setMinimumSize(800, 600)
        self.resize(1000, 700)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(10, 10, 10, 10)

        splitter = QSplitter(Qt.Orientation.Horizontal)
        
        self.stack_widget = StackWidget(self.data_manager)
        self.queue_widget = QueueWidget(self.data_manager)
        
        stack_container = QWidget()
        stack_layout = QVBoxLayout(stack_container)
        stack_layout.setContentsMargins(5, 5, 5, 5)
        stack_layout.addWidget(self.stack_widget)
        
        queue_container = QWidget()
        queue_layout = QVBoxLayout(queue_container)
        queue_layout.setContentsMargins(5, 5, 5, 5)
        queue_layout.addWidget(self.queue_widget)
        
        splitter.addWidget(stack_container)
        splitter.addWidget(queue_container)
        splitter.setSizes([500, 500])
        
        main_layout.addWidget(splitter)

        self.setStyleSheet("""
            QMainWindow {
                background-color: #f5f5f5;
            }
            QWidget {
                font-family: 'Microsoft YaHei';
            }
        """)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_pos = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.drag_pos is not None:
            self.move(event.globalPosition().toPoint() - self.drag_pos)
        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self.drag_pos = None
        super().mouseReleaseEvent(event)

    def closeEvent(self, event):
        self.data_manager.save()
        super().closeEvent(event)
