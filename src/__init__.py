# -*- coding: UTF-8 -*-

import os
import sys
try:
    os.chdir(os.path.dirname(__file__)) # 更改工作目录，指向正确的当前文件夹，才能读取 database.db
    sys.path.append(os.path.dirname(__file__)) # 将当前目录导入 python 寻找 package 和 moduel 的变量
except:
    print('更改使用路径失败，不过没关系')

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

from moduels.component.NormalValue import 常量
from moduels.gui.MainWindow import MainWindow


############# 程序入口 ################

def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    常量.mainWindow = mainWindow
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
