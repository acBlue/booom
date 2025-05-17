import os
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QPixmap, QFont, QColor
from PyQt5.QtCore import Qt, QSize


class StatusIndicator(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumWidth(100)  # 给状态栏一个初始最小宽度

        self._is_normal = True
        self._status_text = "状态正常"

        # 布局：垂直排列图标和文字
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)  # 无内边距
        layout.setSpacing(2)  # 图标和文字之间的间距

        # 状态图标 QLabel
        self.icon_label = QLabel()
        # 图标内容在其 QLabel 内的对齐方式 (如果 pixmap 小于 QLabel 尺寸，这会起作用)
        # 对于固定尺寸的 QLabel 和 scaled pixmap，主要影响由 addWidget 的对齐参数决定
        self.icon_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.icon_label.setFixedSize(QSize(24, 24))  # 固定图标大小

        # 状态文字 QLabel
        self.text_label = QLabel(self._status_text)
        # 文字内容在其 QLabel 内的对齐方式
        self.text_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.text_label.setFont(QFont("Arial", 8))
        self.text_label.setWordWrap(True)

        # 将 QLabel 组件添加到 QVBoxLayout 时，指定它们靠右对齐
        layout.addWidget(self.icon_label, 0, Qt.AlignRight)
        layout.addWidget(self.text_label, 0, Qt.AlignRight)

        self.setLayout(layout)

        self._update_status_display()  # 初始化显示

    def setStatus(self, is_normal, text):
        self._is_normal = is_normal
        self._status_text = text
        self._update_status_display()
        self.updateGeometry()

    def _update_status_display(self):
        self.text_label.setText(self._status_text)
        status_icon_name = "status_ok.png" if self._is_normal else "status_error.png"

        icon_path_relative_to_project_root = os.path.join("resources", status_icon_name)
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        icon_path_absolute = os.path.join(project_root, icon_path_relative_to_project_root)

        if os.path.exists(icon_path_absolute):
            pixmap = QPixmap(icon_path_absolute)
            self.icon_label.setPixmap(
                pixmap.scaled(self.icon_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        else:
            fallback_icon_text = "✔" if self._is_normal else "✖"
            self.icon_label.setText(fallback_icon_text)
            self.icon_label.setFont(QFont("Arial", 14))
            print(f"警告: 状态图标 {status_icon_name} 未找到于 {icon_path_absolute}. 使用文本回退.")

    def sizeHint(self):
        text_metrics = self.text_label.fontMetrics()
        text_rect = text_metrics.boundingRect(0, 0, self.text_label.width() if self.text_label.width() > 0 else 80, 0,
                                              Qt.TextWordWrap, self.text_label.text())
        text_height_adjusted = text_rect.height() + 5

        icon_height = self.icon_label.height()
        total_height = icon_height + self.layout().spacing() + text_height_adjusted

        # 宽度由内容决定，但由于内容是右对齐的，所以 sizeHint 可以反映内容本身的宽度
        # text_label 的宽度在 wordWrap 后可能会变化，取其 sizeHint 或 minimumSizeHint
        # 这里简单估算，实际显示时 QSizePolicy 和布局会处理
        content_width = 0
        if self.icon_label.pixmap() or self.icon_label.text():
            content_width = max(content_width, self.icon_label.sizeHint().width())
        if self.text_label.text():
            # 估算文本宽度，如果文本很长且换行，其宽度会接近 text_label 的有效宽度
            # 但由于是右对齐，我们更关心它实际占多少
            text_content_width = text_metrics.horizontalAdvance(self.text_label.text().split('\n')[0])  # 估算最长一行 (简化)
            content_width = max(content_width, text_content_width)

        min_w = max(80, content_width + 10)  # 加一点padding
        return QSize(int(min_w), int(total_height))