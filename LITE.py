from PyQt5 import QtCore, QtGui, QtWidgets
from LITE_UI import Ui_LITE
from LITE_Helpers import TextHelper, PutHtml
#from ExampleDisplayWidget import Ui_ExampleWidget
from FormatStyle import FormatStyle
from FormattedExample import FormattedExample
from ScriptManager import ScriptManager
import clipboard
import webbrowser

formatStyles = [] #array of FormatStyle
dataSources = [] #array of tuples of (pruned file name, full path)
exampleHistory = [] #array of FormattedExample, updated on Copy to Clipboard
sm = ScriptManager()
currentExample = FormattedExample("", FormatStyle("")) #initialized with empty values

#--helper methods--
def initialize_globals():
    #initialize default format styles
    formatStyles.append(FormatStyle("3-line GSRL standard"))
    formatStyles.append(FormatStyle("4-line GSRL standard"))
    currentExample.selectedFormatStyle = formatStyles[0] #default format style is "3-line GSRL standard"
    #ui.exampleListView.setModel(Ui_ExampleWidget()) #incomplete, commented out intentionally


def refresh_ui():
    #empty and replace stylenames in stylename combobox
    ui.formatStyleComboBox.clear()
    for fs in formatStyles:
        ui.formatStyleComboBox.addItem(fs.stylename)
    ui.formatStyleComboBox.setCurrentIndex(
        ui.formatStyleComboBox.findText(currentExample.selectedFormatStyle.stylename))

    #empty and replace data sources in data source combobox
    ui.dataSourceComboBox.clear()
    for ds in dataSources:
        ui.dataSourceComboBox.addItem(ds[0])
    if ui.dataSourceComboBox.count() > 1 :
        ui.dataSourceComboBox.setCurrentIndex(
            ui.dataSourceComboBox.findText(TextHelper.pruneFileName(currentExample.dataSource))) #set index to selected item

    ui.outputPreviewTextEdit.setText(sm.convert_text(currentExample))

#--user actions--
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
    
    if ui.dataSourceReferenceBox.isChecked():
        currentExample.dataSourceRef = str(ui.dataSourceNameComboBox.currentText())
    else:
        currentExample.dataSourceRef = ""

    #format style combobox
    currentExample.selectedFormatStyle = next((fs for fs in formatStyles if fs.stylename == ui.formatStyleComboBox.currentText()), None)

    #data source combobox
    if len(dataSources) > 0:
        currentExample.dataSource = dataSources[ui.dataSourceComboBox.currentIndex()][1]
    
    refresh_ui()
    
def retrieve_clipboard():
    if currentExample.dataSource == "":
        global errormessagedialog #Must be global to persist after the function completes. This is bad practice, and will be changed before final version.
        errormessagedialog = QtWidgets.QErrorMessage()
        errormessagedialog.showMessage('Please select a data source.')
    else:
        currentExample.pastedText = clipboard.paste()
        ui.clipboardContentTextEdit.setText(currentExample.pastedText)
        ui.outputPreviewTextEdit.setText(sm.convert_text(currentExample))

def copy_to_clipboard():
    PutHtml(currentExample.pastedText) #outputs into the html portion of the clipboard
    exampleHistory.append(currentExample)

def get_data_source():
    currentExample.dataSource, _ = QtWidgets.QFileDialog.getOpenFileName(ui.AddSourceButton, 'Get Data Source', '', 'Flextext files (*.flextext)')
    dataSources.append((TextHelper.pruneFileName(currentExample.dataSource), currentExample.dataSource))
    
    refresh_ui()

#--event connections--
def set_event_connections():
    #does not interact with the model
    ui.helpButton.clicked.connect(lambda: webbrowser.open('https://github.com/SamDelaney/LITE/wiki'))
    
    #calling methods from the model
    ui.pasteButton.clicked.connect(lambda: retrieve_clipboard())
    ui.copyButton.clicked.connect(lambda: copy_to_clipboard())
    ui.AddSourceButton.clicked.connect(lambda: get_data_source())

    #language name option radio buttons
    ui.noLangNameButton.clicked.connect(lambda: FEOptionsUpdated())
    ui.langNameFirstLineButton.clicked.connect(lambda: FEOptionsUpdated())
    ui.langNameOnRightButton.clicked.connect(lambda: FEOptionsUpdated())
    #other formatted example options
    ui.ungrammaticalBox.clicked.connect(lambda: FEOptionsUpdated())
    ui.litTranslationBox.clicked.connect(lambda: FEOptionsUpdated())

    #comboboxes
    ui.dataSourceReferenceBox.clicked.connect(lambda: FEOptionsUpdated())
    ui.dataSourceComboBox.activated.connect(lambda: FEOptionsUpdated())
    ui.formatStyleComboBox.activated.connect(lambda: FEOptionsUpdated())
    

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

    
