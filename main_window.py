from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QStackedWidget
from PyQt5.QtCore import Qt

from widgets.header_widget import HeaderWidget
from widgets.menu_widget import MenuWidget  # 使用封装好的 MenuWidget
# 或者直接使用 QListWidget
# from PyQt5.QtWidgets import QListWidget, QListWidgetItem

from widgets.pages.home_page import HomePage
from widgets.pages.settings_page import SettingsPage
from widgets.pages.data_analysis_page import DataAnalysisPage
from widgets.pages.about_page import AboutPage


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("我的模块化应用")
        self.setGeometry(100, 100, 800, 600)

        self.initUI()

    def initUI(self):
        # --- 主体布局 ---
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # 整体垂直布局: 顶部导航栏 + (左侧菜单 + 右侧内容)
        overall_layout = QVBoxLayout(central_widget)
        overall_layout.setContentsMargins(0, 0, 0, 0)  # 移除边距，让导航栏紧贴顶部
        overall_layout.setSpacing(0)  # 移除组件间距

        # --- 顶部导航栏 ---
        self.header = HeaderWidget()
        overall_layout.addWidget(self.header)

        # --- 内容区域布局 (菜单 + 主界面) ---
        content_widget = QWidget()  # 用于包含菜单和主界面的容器
        content_layout = QHBoxLayout(content_widget)
        content_layout.setContentsMargins(5, 5, 5, 5)  # 给内容区一点边距
        content_layout.setSpacing(5)  # 菜单和主界面之间的间距

        # --- 左侧菜单栏 ---
        self.menu_list = MenuWidget()  # 使用封装的 MenuWidget
        # 如果不使用 MenuWidget，则像之前一样创建 QListWidget
        # self.menu_list = QListWidget()
        # self.menu_list.setFixedWidth(200)
        # menu_items = ["主页", "设置", "数据分析", "关于"]
        # for item_text in menu_items:
        #     self.menu_list.addItem(QListWidgetItem(item_text))

        content_layout.addWidget(self.menu_list)

        # --- 右侧主界面区域 (使用 QStackedWidget) ---
        self.stacked_widget = QStackedWidget()

        # 创建页面实例
        self.home_page = HomePage()
        self.settings_page = SettingsPage()
        self.data_analysis_page = DataAnalysisPage()
        self.about_page = AboutPage()

        # 将页面添加到 QStackedWidget
        self.stacked_widget.addWidget(self.home_page)
        self.stacked_widget.addWidget(self.settings_page)
        self.stacked_widget.addWidget(self.data_analysis_page)
        self.stacked_widget.addWidget(self.about_page)

        content_layout.addWidget(self.stacked_widget)

        overall_layout.addWidget(content_widget)  # 将内容区域添加到整体布局

        # --- 连接信号和槽 ---
        self.menu_list.currentRowChanged.connect(self.display_page)

        # 默认选中第一个菜单项
        self.menu_list.setCurrentRow(0)
        self.display_page(0)  # 初始化显示第一个页面

    def display_page(self, index):
        # item_id = self.menu_list.get_item_id(index) # 如果 MenuWidget 中使用了 id
        # print(f"Switching to page index: {index}, id: {item_id}")
        self.stacked_widget.setCurrentIndex(index)