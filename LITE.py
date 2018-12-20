# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainAppDesign.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from LITE_UI import Ui_LITE

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LITE = QtWidgets.QMainWindow()
    ui = Ui_LITE()
    ui.setupUi(LITE)
    LITE.show()
    sys.exit(app.exec_())
