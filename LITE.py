from PyQt5 import QtCore, QtGui, QtWidgets
from LITE_UI import Ui_LITE
from FormatStyle import FormatStyle
from FormattedExample import FormattedExample
from ScriptManager import ScriptManager
import clipboard

formatStyles = []
sm = ScriptManager()
currentExample = FormattedExample("", FormatStyle("")) #initialized with empty values

def initialize_globals():
    #initialize default format styles
    formatStyles.append(FormatStyle("3-line GSRL standard"))
    formatStyles.append(FormatStyle("4-line GSRL standard"))
    currentExample.selectedFormatStyle = formatStyles[0]

def refresh_ui():
    for fs in formatStyles:
        ui.formatStyleComboBox.addItem(fs.stylename)
    ui.outputPreviewTextEdit.setText(sm.convert_text(currentExample))

def retrieve_clipboard():
    currentExample.pastedText = clipboard.paste()
    ui.clipboardContentTextEdit.setText(currentExample.pastedText)
    ui.outputPreviewTextEdit.setText(sm.convert_text(currentExample))

def copy_to_clipboard():
    clipboard.copy(currentExample.pastedText)

def set_event_connections():
    ui.pasteButton.clicked.connect(lambda: retrieve_clipboard())
    ui.copyButton.clicked.connect(lambda: copy_to_clipboard())

if __name__ ==  "__main__":
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

    
