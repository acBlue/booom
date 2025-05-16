from PyQt5.QtWidgets import QListWidget, QListWidgetItem
from PyQt5.QtGui import QFont #, QIcon (如果需要图标)
# from PyQt5.QtCore import QSize (如果需要设置图标大小)

class MenuWidget(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedWidth(200)
        # self.setFont(QFont("Arial", 12))

        self.menu_items_data = [
            {"text": "主页", "id": "home"},
            {"text": "设置", "id": "settings"},
            {"text": "数据分析", "id": "data_analysis"},
            {"text": "关于", "id": "about"}
        ]

        for item_data in self.menu_items_data:
            list_item = QListWidgetItem(item_data["text"])
            # list_item.setData(Qt.UserRole, item_data["id"]) # 可以用ID来识别，而不是索引
            # if "icon" in item_data and item_data["icon"]:
            #     list_item.setIcon(QIcon(item_data["icon"]))
            self.addItem(list_item)

    def get_item_id(self, index):
        if 0 <= index < self.count():
            return self.menu_items_data[index]["id"]
        return None