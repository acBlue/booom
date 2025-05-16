from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

class SettingsPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        label = QLabel("<h2>设置中心</h2><p>在这里配置你的应用参数。</p>")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)
        self.setObjectName("SettingsPage")