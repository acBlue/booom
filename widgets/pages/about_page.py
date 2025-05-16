from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

class AboutPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        label = QLabel("<h3>关于我们</h3><p>这是一个使用 PyQt 和 qt-material 构建的应用示例。</p>")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)
        self.setObjectName("AboutPage")