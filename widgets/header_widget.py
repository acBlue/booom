import os
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QLabel, QFrame,
                             QSizePolicy, QSpacerItem)
from PyQt5.QtGui import QFont  # QPixmap, QColor 不再直接在本文件中使用
from PyQt5.QtCore import Qt  # QSize 不再直接在本文件中使用

# 从同一目录下导入 LogoWidget 和新的 StatusIndicatorWidget
from .logo_widget import LogoWidget
from .status_indicator_widget import StatusIndicator  # <<< 新增导入


class HeaderWidget(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedHeight(65)
        self.setObjectName("HeaderWidget")

        # 背景图片设置 (与之前相同)
        background_image_path_relative = os.path.join("resources", "header_background.png")
        project_root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        background_image_path_abs = os.path.join(project_root_dir, background_image_path_relative)

        common_label_style = "background-color: transparent;"

        if os.path.exists(background_image_path_abs):
            stylesheet_path = background_image_path_abs.replace(os.sep, '/')
            self.setStyleSheet(f"""
                #HeaderWidget {{
                    border-image: url({stylesheet_path}) 0 0 0 0 stretch stretch;
                    border-bottom: 1px solid #B0B0B0; 
                }}
                QLabel {{
                    {common_label_style}
                }}
            """)
        else:
            print(f"警告: 背景图片未找到于 {background_image_path_abs}")
            self.setStyleSheet(f"""
                #HeaderWidget {{
                    background-color: #F0F0F0; 
                    border-bottom: 1px solid #B0B0B0;
                }}
                QLabel {{
                    {common_label_style}
                }}
            """)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 0, 10, 0)
        layout.setSpacing(10)

        # 应用 Logo
        self.app_logo = LogoWidget(logo_height=self.height() - 25)

        # 应用名称或标题
        self.title_label = QLabel("我的应用")
        self.title_label.setFont(QFont("Arial", 16, QFont.Bold))
        # self.title_label.setStyleSheet("color: white;") # 如果背景图暗

        # 状态指示器 (使用导入的类)
        self.status_indicator = StatusIndicator()
        self.status_indicator.setStatus(True, "系统状态正常")

        # --- 布局 ---
        layout.addWidget(self.app_logo)
        layout.addWidget(self.title_label)

        spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        layout.addSpacerItem(spacer)

        layout.addWidget(self.status_indicator)

        self.setLayout(layout)

    def set_application_status(self, is_normal, status_text):
        self.status_indicator.setStatus(is_normal, status_text)