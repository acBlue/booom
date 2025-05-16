from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

class DataAnalysisPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        label = QLabel("<h2>数据分析模块</h2><p>图表和数据将在这里展示。</p>")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)
        self.setObjectName("DataAnalysisPage")