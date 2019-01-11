from PyQt5 import QtCore, QtGui, QtWidgets
from LITE_UI import Ui_LITE
#from ExampleDisplayWidget import Ui_ExampleWidget
from FormatStyle import FormatStyle
from FormattedExample import FormattedExample
from ScriptManager import ScriptManager
import clipboard

formatStyles = []
exampleHistory = []
sm = ScriptManager()
currentExample = FormattedExample("", FormatStyle("")) #initialized with empty values

def initialize_globals():
    #initialize default format styles
    formatStyles.append(FormatStyle("3-line GSRL standard"))
    formatStyles.append(FormatStyle("4-line GSRL standard"))
    currentExample.selectedFormatStyle = formatStyles[0]
    #ui.exampleListView.setModel(Ui_ExampleWidget())

#returns 0 if no language name
#returns 1 if include language name as first line
#returns 2 if include language name on right side
def getLangNameOption():
    if ui.noLangNameButton.isChecked():
        currentExample.langNameOption = 0
    if ui.langNameFirstLineButton.isChecked():
        currentExample.langNameOption = 1
    if ui.langNameOnRightButton.isChecked():
        currentExample.langNameOption = 2
    refresh_ui()

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
    exampleHistory.append(currentExample)

def set_event_connections():
    ui.pasteButton.clicked.connect(lambda: retrieve_clipboard())
    ui.copyButton.clicked.connect(lambda: copy_to_clipboard())

    #language name option radio buttons
    ui.noLangNameButton.clicked.connect(lambda: getLangNameOption())
    ui.langNameFirstLineButton.clicked.connect(lambda: getLangNameOption())
    ui.langNameOnRightButton.clicked.connect(lambda: getLangNameOption())
    

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

    
