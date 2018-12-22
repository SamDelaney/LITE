from PyQt5 import QtCore, QtGui, QtWidgets
from LITE_UI import Ui_LITE
from FormatStyle import FormatStyle
import clipboard

formatStyles = []

def initialize_globals():
    #initialize default format styles
    formatStyles.append(FormatStyle("3-line GSRL standard"))
    formatStyles.append(FormatStyle("4-line GSRL standard"))

def refresh_ui():
    for fs in formatStyles:
        ui.formatStyleComboBox.addItem(fs.stylename)

def retrieve_clipboard():
    ui.clipboardContentTextEdit.setText(clipboard.paste())

def set_event_connections():
    ui.pasteButton.clicked.connect(lambda: retrieve_clipboard())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LITE = QtWidgets.QMainWindow()
    ui = Ui_LITE()
    ui.setupUi(LITE)
    initialize_globals()
    set_event_connections()
    LITE.show()
    refresh_ui()
    sys.exit(app.exec_())

    
