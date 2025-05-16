from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

class HomePage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        label = QLabel("<h1>欢迎来到主页</h1><p>这里是主页内容。</p>")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)
        self.setObjectName("HomePage") # 用于样式或识别