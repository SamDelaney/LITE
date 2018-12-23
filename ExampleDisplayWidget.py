# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ExampleDisplay.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ExampleDisplay(object):
    def setupUi(self, ExampleDisplay):
        ExampleDisplay.setObjectName("ExampleDisplay")
        ExampleDisplay.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(ExampleDisplay)
        self.verticalLayout.setObjectName("verticalLayout")
        self.exampleLanguageLabel = QtWidgets.QLabel(ExampleDisplay)
        self.exampleLanguageLabel.setObjectName("exampleLanguageLabel")
        self.verticalLayout.addWidget(self.exampleLanguageLabel)
        self.exampleTextBrowser = QtWidgets.QTextBrowser(ExampleDisplay)
        self.exampleTextBrowser.setObjectName("exampleTextBrowser")
        self.verticalLayout.addWidget(self.exampleTextBrowser)
        self.buttonLayout = QtWidgets.QHBoxLayout()
        self.buttonLayout.setObjectName("buttonLayout")
        self.copyButton = QtWidgets.QPushButton(ExampleDisplay)
        self.copyButton.setObjectName("copyButton")
        self.buttonLayout.addWidget(self.copyButton, 0, QtCore.Qt.AlignRight)
        self.loadAndEditButton = QtWidgets.QPushButton(ExampleDisplay)
        self.loadAndEditButton.setObjectName("loadAndEditButton")
        self.buttonLayout.addWidget(self.loadAndEditButton, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout.addLayout(self.buttonLayout)

        self.retranslateUi(ExampleDisplay)
        QtCore.QMetaObject.connectSlotsByName(ExampleDisplay)

    def retranslateUi(self, ExampleDisplay):
        _translate = QtCore.QCoreApplication.translate
        ExampleDisplay.setWindowTitle(_translate("ExampleDisplay", "ExampleDisplay"))
        self.exampleLanguageLabel.setText(_translate("ExampleDisplay", "Placeholder Language Name"))
        self.copyButton.setText(_translate("ExampleDisplay", "Copy to Clipboard"))
        self.loadAndEditButton.setText(_translate("ExampleDisplay", "Load and Edit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ExampleDisplay = QtWidgets.QWidget()
    ui = Ui_ExampleDisplay()
    ui.setupUi(ExampleDisplay)
    ExampleDisplay.show()
    sys.exit(app.exec_())

