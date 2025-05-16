import os
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QFrame
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt, QSize

class HeaderWidget(QFrame): # 使用 QFrame 可以更容易地设置边框和背景
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedHeight(60) # 固定头部高度
        self.setObjectName("HeaderWidget") # 用于 qt-material 样式化
        # self.setStyleSheet("#HeaderWidget { background-color: #333; border-bottom: 1px solid #555; }") # 可选的自定义样式

        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 0, 10, 0) # 左、上、右、下边距

        # Logo
        self.logo_label = QLabel()
        logo_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "resources", "logo.png") # 获取resources/logo.png路径

        if os.path.exists(logo_path):
            pixmap = QPixmap(logo_path)
            self.logo_label.setPixmap(pixmap.scaled(QSize(40, 40), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        else:
            self.logo_label.setText("LOGO")
            self.logo_label.setFont(QFont("Arial", 16, QFont.Bold))
            self.logo_label.setStyleSheet("color: white;") # 如果背景深色
            self.logo_label.setStyleSheet("background-color: transparent;") # 如果背景浅色

        # 应用名称或标题
        self.title_label = QLabel("我的应用")
        self.title_label.setFont(QFont("Arial", 14, QFont.Bold))
        # self.title_label.setStyleSheet("color: white;") # 如果背景深色
        self.title_label.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.logo_label)
        layout.addSpacing(10) # Logo 和标题之间的间距
        layout.addWidget(self.title_label, 1) # 标题占据剩余空间，并居中
        layout.addStretch(0) # 确保标题不会被过度拉伸（如果右侧有其他元素）

        self.setLayout(layout)