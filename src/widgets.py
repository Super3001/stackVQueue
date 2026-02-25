from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
    QTextEdit, QScrollArea, QFrame, QMessageBox, QPushButton
)
from PyQt6.QtCore import Qt, pyqtSignal, QTimer
from PyQt6.QtGui import QFont
from src.data_model import DataItem


class ItemWidget(QFrame):
    text_changed = pyqtSignal(object, str)
    move_up = pyqtSignal(object)
    move_down = pyqtSignal(object)

    def __init__(self, item: DataItem, parent=None):
        super().__init__(parent)
        self.item = item
        self._save_timer = QTimer()
        self._save_timer.setSingleShot(True)
        self._save_timer.timeout.connect(self._emit_text_changed)
        self._pending_text = None
        self.setFrameStyle(QFrame.Shape.Box | QFrame.Shadow.Raised)
        self.setLineWidth(2)
        self.setStyleSheet("""
            ItemWidget {
                background-color: #f0f8ff;
                border: 2px solid #4682b4;
                border-radius: 5px;
                margin: 2px;
            }
            ItemWidget:hover {
                background-color: #e6f2ff;
                border-color: #1e90ff;
            }
        """)
        self.setMinimumWidth(120)
        self.setMaximumWidth(200)
        self.setup_ui()
        self.setMouseTracking(True)

    def setup_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(5, 5, 5, 5)
        
        button_layout = QHBoxLayout()
        button_layout.setContentsMargins(0, 0, 0, 0)
        button_layout.setAlignment(Qt.AlignmentFlag.AlignRight)
        
        self.up_btn = QPushButton("↑")
        self.up_btn.setFont(QFont('Microsoft YaHei', 8))
        self.up_btn.setFixedSize(20, 20)
        self.up_btn.setStyleSheet("""
            QPushButton {
                background-color: #4682b4;
                color: white;
                border: none;
                border-radius: 3px;
            }
            QPushButton:hover {
                background-color: #1e90ff;
            }
        """)
        self.up_btn.clicked.connect(lambda: self.move_up.emit(self.item))
        self.up_btn.hide()
        button_layout.addWidget(self.up_btn)
        
        self.down_btn = QPushButton("↓")
        self.down_btn.setFont(QFont('Microsoft YaHei', 8))
        self.down_btn.setFixedSize(20, 20)
        self.down_btn.setStyleSheet("""
            QPushButton {
                background-color: #4682b4;
                color: white;
                border: none;
                border-radius: 3px;
            }
            QPushButton:hover {
                background-color: #1e90ff;
            }
        """)
        self.down_btn.clicked.connect(lambda: self.move_down.emit(self.item))
        self.down_btn.hide()
        button_layout.addWidget(self.down_btn)
        
        main_layout.addLayout(button_layout)
        
        self.text_edit = QTextEdit()
        self.text_edit.setPlainText(self.item.text)
        self.text_edit.setFont(QFont('Microsoft YaHei', 12))
        self.text_edit.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.text_edit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.text_edit.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.text_edit.textChanged.connect(self.on_text_changed)
        self.text_edit.setMaximumHeight(80)
        main_layout.addWidget(self.text_edit)

    def on_text_changed(self):
        new_text = self.text_edit.toPlainText()
        if new_text != self.item.text:
            self._pending_text = new_text
            self._save_timer.start(500)

    def _emit_text_changed(self):
        if self._pending_text is not None and self._pending_text != self.item.text:
            self.text_changed.emit(self.item, self._pending_text)
            self._pending_text = None

    def enterEvent(self, event):
        tooltip = f"入栈/入队时间: {self.item.push_time}\n修改时间: {self.item.modify_time}"
        if self.item.pop_time:
            tooltip += f"\n出栈/出队时间: {self.item.pop_time}"
        self.setToolTip(tooltip)
        self.up_btn.show()
        self.down_btn.show()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.up_btn.hide()
        self.down_btn.hide()
        super().leaveEvent(event)


class StackWidget(QWidget):
    def __init__(self, data_manager, parent=None):
        super().__init__(parent)
        self.data_manager = data_manager
        self.item_widgets: list[ItemWidget] = []
        self.setup_ui()

    def setup_ui(self):
        main_layout = QVBoxLayout(self)
        
        title = QLabel("Stack (栈)")
        title.setFont(QFont('Microsoft YaHei', 14, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet("QScrollArea { border: 1px solid #ccc; }")
        
        self.scroll_content = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_content)
        self.scroll_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.scroll_area.setWidget(self.scroll_content)
        main_layout.addWidget(self.scroll_area)

        btn_layout = QHBoxLayout()
        self.push_btn = QLabel("入栈 (Push)")
        self.push_btn.setFont(QFont('Microsoft YaHei', 11))
        self.push_btn.setStyleSheet("""
            QLabel {
                background-color: #4CAF50;
                color: white;
                padding: 8px 16px;
                border-radius: 4px;
            }
            QLabel:hover {
                background-color: #45a049;
            }
        """)
        self.push_btn.mousePressEvent = self.on_push
        btn_layout.addWidget(self.push_btn)

        self.pop_btn = QLabel("出栈 (Pop)")
        self.pop_btn.setFont(QFont('Microsoft YaHei', 11))
        self.pop_btn.setStyleSheet("""
            QLabel {
                background-color: #f44336;
                color: white;
                padding: 8px 16px;
                border-radius: 4px;
            }
            QLabel:hover {
                background-color: #da190b;
            }
        """)
        self.pop_btn.mousePressEvent = self.on_pop
        btn_layout.addWidget(self.pop_btn)
        main_layout.addLayout(btn_layout)

        self.load_items()

    def load_items(self):
        for widget in self.item_widgets:
            widget.deleteLater()
        self.item_widgets.clear()
        
        for item in self.data_manager.stack_items:
            self.add_item_widget(item, from_load=True)

    def add_item_widget(self, item: DataItem, from_load=False):
        widget = ItemWidget(item)
        widget.text_changed.connect(self.on_item_text_changed)
        widget.move_up.connect(self.on_move_up)
        widget.move_down.connect(self.on_move_down)
        if from_load:
            self.scroll_layout.addWidget(widget)
            self.item_widgets.append(widget)
        else:
            self.scroll_layout.insertWidget(0, widget)
            self.item_widgets.insert(0, widget)

    def on_push(self, event):
        from PyQt6.QtWidgets import QInputDialog
        text, ok = QInputDialog.getText(self, '入栈', '请输入内容:')
        if ok and text:
            item = self.data_manager.push_stack(text)
            self.add_item_widget(item)

    def on_pop(self, event):
        if self.item_widgets:
            widget = self.item_widgets.pop(0)
            widget.deleteLater()
            self.data_manager.pop_stack()
        else:
            QMessageBox.information(self, '提示', '栈为空!')

    def on_item_text_changed(self, item: DataItem, new_text: str):
        self.data_manager.update_item_text(item, new_text)

    def on_move_up(self, item: DataItem):
        if item in self.data_manager.stack_items:
            index = self.data_manager.stack_items.index(item)
            if index > 0:
                self.data_manager.move_stack_item(index, -1)
                self.load_items()

    def on_move_down(self, item: DataItem):
        if item in self.data_manager.stack_items:
            index = self.data_manager.stack_items.index(item)
            if index < len(self.data_manager.stack_items) - 1:
                self.data_manager.move_stack_item(index, 1)
                self.load_items()


class QueueWidget(QWidget):
    def __init__(self, data_manager, parent=None):
        super().__init__(parent)
        self.data_manager = data_manager
        self.item_widgets: list[ItemWidget] = []
        self.setup_ui()

    def setup_ui(self):
        main_layout = QVBoxLayout(self)
        
        title = QLabel("Queue (队列)")
        title.setFont(QFont('Microsoft YaHei', 14, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet("QScrollArea { border: 1px solid #ccc; }")
        
        self.scroll_content = QWidget()
        self.scroll_layout = QHBoxLayout(self.scroll_content)
        self.scroll_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.scroll_area.setWidget(self.scroll_content)
        main_layout.addWidget(self.scroll_area)

        btn_layout = QHBoxLayout()
        self.enqueue_btn = QLabel("入队 (Enqueue)")
        self.enqueue_btn.setFont(QFont('Microsoft YaHei', 11))
        self.enqueue_btn.setStyleSheet("""
            QLabel {
                background-color: #4CAF50;
                color: white;
                padding: 8px 16px;
                border-radius: 4px;
            }
            QLabel:hover {
                background-color: #45a049;
            }
        """)
        self.enqueue_btn.mousePressEvent = self.on_enqueue
        btn_layout.addWidget(self.enqueue_btn)

        self.dequeue_btn = QLabel("出队 (Dequeue)")
        self.dequeue_btn.setFont(QFont('Microsoft YaHei', 11))
        self.dequeue_btn.setStyleSheet("""
            QLabel {
                background-color: #f44336;
                color: white;
                padding: 8px 16px;
                border-radius: 4px;
            }
            QLabel:hover {
                background-color: #da190b;
            }
        """)
        self.dequeue_btn.mousePressEvent = self.on_dequeue
        btn_layout.addWidget(self.dequeue_btn)
        main_layout.addLayout(btn_layout)

        self.load_items()

    def load_items(self):
        for widget in self.item_widgets:
            widget.deleteLater()
        self.item_widgets.clear()
        
        for item in self.data_manager.queue_items:
            self.add_item_widget(item)

    def add_item_widget(self, item: DataItem):
        widget = ItemWidget(item)
        widget.text_changed.connect(self.on_item_text_changed)
        widget.move_up.connect(self.on_move_left)
        widget.move_down.connect(self.on_move_right)
        self.scroll_layout.addWidget(widget)
        self.item_widgets.append(widget)

    def on_enqueue(self, event):
        from PyQt6.QtWidgets import QInputDialog
        text, ok = QInputDialog.getText(self, '入队', '请输入内容:')
        if ok and text:
            item = self.data_manager.enqueue(text)
            self.add_item_widget(item)

    def on_dequeue(self, event):
        if self.item_widgets:
            widget = self.item_widgets.pop(0)
            widget.deleteLater()
            self.data_manager.dequeue()
        else:
            QMessageBox.information(self, '提示', '队列为空!')

    def on_item_text_changed(self, item: DataItem, new_text: str):
        self.data_manager.update_item_text(item, new_text)

    def on_move_left(self, item: DataItem):
        if item in self.data_manager.queue_items:
            index = self.data_manager.queue_items.index(item)
            if index > 0:
                self.data_manager.move_queue_item(index, -1)
                self.load_items()

    def on_move_right(self, item: DataItem):
        if item in self.data_manager.queue_items:
            index = self.data_manager.queue_items.index(item)
            if index < len(self.data_manager.queue_items) - 1:
                self.data_manager.move_queue_item(index, 1)
                self.load_items()
