import sys
import os

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication
# from PyQt5.QtGui import QFont # 如果需要全局字体
from qt_material import apply_stylesheet

# 确保Python可以找到你的模块 (如果你的项目不在PYTHONPATH中)
# 通常，如果你的项目根目录是 my_material_app，并且你从 my_material_app 的上一级目录运行，
# 或者 my_material_app 本身在 PYTHONPATH 中，这是不需要的。
# 但为了保险起见，或者如果你的运行方式不同，可以添加：
# current_dir = os.path.dirname(os.path.abspath(__file__))
# sys.path.append(os.path.dirname(current_dir)) # 如果main.py在my_material_app内
# sys.path.append(current_dir) # 如果my_material_app在PYTHONPATH且从其内部运行

from main_window import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 应用 qt-material 主题
    #theme_file = 'dark_amber.xml'
    theme_file = 'light_blue.xml'
    # theme_file = os.path.join('path', 'to', 'your', 'custom_theme.xml') # 自定义主题路径
    apply_stylesheet(app, theme=theme_file)

    # 可选: 设置全局字体
    app_font = QFont("Microsoft YaHei", 10)
    app.setFont(app_font)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())