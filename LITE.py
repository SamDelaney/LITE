from PyQt5 import QtCore, QtGui, QtWidgets
from LITE_UI import Ui_LITE
#from ExampleDisplayWidget import Ui_ExampleWidget
from FormatStyle import FormatStyle
from FormattedExample import FormattedExample
from ScriptManager import ScriptManager
import clipboard
import webbrowser

formatStyles = []
exampleHistory = []
sm = ScriptManager()
currentExample = FormattedExample("", FormatStyle("")) #initialized with empty values

def initialize_globals():
    #initialize default format styles
    formatStyles.append(FormatStyle("3-line GSRL standard"))
    formatStyles.append(FormatStyle("4-line GSRL standard"))
    currentExample.selectedFormatStyle = formatStyles[0]
    #ui.exampleListView.setModel(Ui_ExampleWidget()) #incomplete, commented out intentionally

def FEOptionsUpdated():
    #language name option radio buttons
    if ui.noLangNameButton.isChecked():
        currentExample.langNameOption = 0
    elif ui.langNameFirstLineButton.isChecked():
        currentExample.langNameOption = 1
    else: #langNameOnRightButton
        currentExample.langNameOption = 2

    #other formatted example options
    currentExample.isUngrammatical = ui.ungrammaticalBox.isChecked()
    currentExample.useLiteralTrans = ui.litTranslationBox.isChecked()
    
    refresh_ui()

def refresh_ui():
    #empty and replace stylenames in stylename combobox
    ui.formatStyleComboBox.clear()
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
    #does not interact with the model
    ui.helpButton.clicked.connect(lambda: webbrowser.open('https://github.com/SamDelaney/LITE/wiki'))
    
    #calling methods from the model
    ui.pasteButton.clicked.connect(lambda: retrieve_clipboard())
    ui.copyButton.clicked.connect(lambda: copy_to_clipboard())

    #language name option radio buttons
    ui.noLangNameButton.clicked.connect(lambda: FEOptionsUpdated())
    ui.langNameFirstLineButton.clicked.connect(lambda: FEOptionsUpdated())
    ui.langNameOnRightButton.clicked.connect(lambda: FEOptionsUpdated())
    #other formatted example options
    ui.ungrammaticalBox.clicked.connect(lambda: FEOptionsUpdated())
    ui.litTranslationBox.clicked.connect(lambda: FEOptionsUpdated())
    

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

    
