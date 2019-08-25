from PyQt5.QtWidgets import *
from ExampleDisplayWidget import Ui_ExampleDisplay

class HistoryWidget(QListWidgetItem):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.lay = QVBoxLayout(self)

    def setupUI(self, ExampleHistory):
        for Example in ExampleHistory:
            addExample(Example)
            
    def addExample(self, Example):
        ExampleDisplay = QtWidgets.QWidget()
        ui = Ui_ExampleDisplay()
        ui.setupUi(ExampleDisplay)
        self.lay.addWidget(ExampleDisplay)

