import os
from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt, QSize


class LogoWidget(QWidget):
    def __init__(self, logo_height=40, parent=None):
        """
        应用Logo组件.
        :param logo_height: Logo的期望高度，宽度将根据图片比例自动调整.
        :param parent: 父组件.
        """
        super().__init__(parent)
        self.logo_label = QLabel(self)

        # 构建logo.png的绝对路径
        # __file__ 是当前文件 (logo_widget.py) 的路径
        # os.path.dirname(__file__) 是 widgets 目录
        # os.path.dirname(os.path.dirname(__file__)) 是 my_material_app 项目根目录
        logo_path_relative_to_project_root = os.path.join("resources", "logo.png")
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        logo_path_absolute = os.path.join(project_root, logo_path_relative_to_project_root)

        if os.path.exists(logo_path_absolute):
            pixmap = QPixmap(logo_path_absolute)
            # 保持Logo高宽比，高度适应Header高度减去一些边距
            self.logo_label.setPixmap(pixmap.scaledToHeight(logo_height, Qt.SmoothTransformation))
            # 你也可以根据需要设置固定尺寸，或者让它基于内容自适应
            # self.logo_label.setFixedSize(pixmap.scaledToHeight(logo_height, Qt.SmoothTransformation).size())
        else:
            self.logo_label.setText("LOGO")
            self.logo_label.setFont(QFont("Arial", 16, QFont.Bold))
            print(f"警告: Logo图片未找到于 {logo_path_absolute}")
            # 如果没有logo图片，可以设置一个最小尺寸
            self.logo_label.setMinimumSize(logo_height * 2, logo_height)

        # 使用一个布局来包裹QLabel，这样更容易控制Widget的大小策略
        layout = QHBoxLayout(self)
        layout.addWidget(self.logo_label)
        layout.setContentsMargins(0, 0, 0, 0)  # 组件内部无边距
        self.setLayout(layout)

    def set_logo_height(self, height):
        """允许外部调整logo高度并重新加载"""
        logo_path_relative_to_project_root = os.path.join("resources", "logo.png")
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        logo_path_absolute = os.path.join(project_root, logo_path_relative_to_project_root)

        if os.path.exists(logo_path_absolute):
            pixmap = QPixmap(logo_path_absolute)
            self.logo_label.setPixmap(pixmap.scaledToHeight(height, Qt.SmoothTransformation))
        else:
            self.logo_label.setMinimumSize(height * 2, height)