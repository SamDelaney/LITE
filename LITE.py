from PyQt5 import QtCore, QtGui, QtWidgets
from LITE_UI import Ui_LITE
from LITE_Helpers import TextHelper, PutHtml
#from ExampleDisplayWidget import Ui_ExampleWidget
from FormatStyle import FormatStyle
from FormattedExample import FormattedExample
from ScriptManager import ScriptManager
import clipboard
import webbrowser
import time
import pickle
import sys

class MainApp(QtWidgets.QApplication):
    formatStyles = [] #array of FormatStyle
    dataSources = [] #array of tuples of (pruned file name, full path)
    exampleHistory = [] #array of FormattedExample, updated on Copy to Clipboard
    sm = ScriptManager()
    currentExample = FormattedExample("", FormatStyle("")) #initialized with empty values
    
    def __init__(self, arg):
        QtWidgets.QApplication.__init__(self, arg)


    #--helper methods--
    def store_data(self):
        data = [self.formatStyles, self.dataSources, self.exampleHistory, self.currentExample]
        with open('LITE_data.pickle', 'wb') as handle:
            pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)
        

    def initialize_globals(self):
        #initialize default format styles
        self.formatStyles.append(FormatStyle("3-line GSRL standard"))
        self.formatStyles.append(FormatStyle("4-line GSRL standard"))
        #ui.exampleListView.setModel(Ui_ExampleWidget()) #incomplete, commented out intentionally

        #retrieves data from pickle file
        with open('LITE_data.pickle', 'rb') as handle:
           data = pickle.load(handle)
        self.formatStyles = data[0]
        self.dataSources = data[1]
        self.exampleHistory = data[2]
        self.currentExample = data[3]
        print(self.currentExample.dataSource)

    def refresh_ui(self):
        #empty and replace stylenames in stylename combobox
        ui.formatStyleComboBox.clear()
        for fs in self.formatStyles:
            ui.formatStyleComboBox.addItem(fs.stylename)
        ui.formatStyleComboBox.setCurrentIndex(
            ui.formatStyleComboBox.findText(self.currentExample.selectedFormatStyle.stylename))

        #empty and replace data sources in data source combobox
        ui.dataSourceComboBox.clear()
        for ds in self.dataSources:
            ui.dataSourceComboBox.addItem(ds[0])
        if ui.dataSourceComboBox.count() > 1 :
            ui.dataSourceComboBox.setCurrentIndex(
                ui.dataSourceComboBox.findText(TextHelper.pruneFileName(self.currentExample.dataSource))) #set index to selected item
            ui.outputPreviewTextEdit.setText(self.sm.convert_text(self.currentExample))
        print(self.currentExample.dataSource)
        

    #--user actions--
    def FEOptionsUpdated(self):
        #language name option radio buttons
        if ui.noLangNameButton.isChecked():
            self.currentExample.langNameOption = 0
        elif ui.langNameFirstLineButton.isChecked():
            self.currentExample.langNameOption = 1
        else: #langNameOnRightButton
            self.currentExample.langNameOption = 2

        #other formatted example options
        self.currentExample.isUngrammatical = ui.ungrammaticalBox.isChecked()
        self.currentExample.useLiteralTrans = ui.litTranslationBox.isChecked()
        
        if ui.dataSourceReferenceBox.isChecked():
            self.currentExample.dataSourceRef = str(ui.dataSourceNameComboBox.currentText())
        else:
            self.currentExample.dataSourceRef = ""

        #format style combobox
        self.currentExample.selectedFormatStyle = next((fs for fs in self.formatStyles if fs.stylename == ui.formatStyleComboBox.currentText()), None)

        #data source combobox
        if len(self.dataSources) > 0:
            self.currentExample.dataSource = self.dataSources[ui.dataSourceComboBox.currentIndex()][1]
        
        self.refresh_ui()
        
    def retrieve_clipboard(self):
        if self.currentExample.dataSource == "":
            global errormessagedialog #Must be global to persist after the function completes. This is bad practice, and will be changed before final version.
            errormessagedialog = QtWidgets.QErrorMessage()
            errormessagedialog.showMessage('Please select a data source.')
        else:
            self.currentExample.pastedText = clipboard.paste()
            ui.clipboardContentTextEdit.setText(self.currentExample.pastedText)
            ui.outputPreviewTextEdit.setText(self.sm.convert_text(self.currentExample))

    def copy_to_clipboard(self):
        #outputs into the html portion of the clipboard
        PutHtml(self.currentExample.pastedText)
        
        #gets time since epoch (time()) and translates it into current time (ctime())
        ui.updateTimeLabel.setText(time.ctime(time.time()))

        #adds current formatted example to history
        self.exampleHistory.append(self.currentExample)
        self.store_data()

    def get_data_source(self):
        self.currentExample.dataSource, _ = QtWidgets.QFileDialog.getOpenFileName(ui.AddSourceButton, 'Get Data Source', '', 'Flextext files (*.flextext)')
        self.dataSources.append((TextHelper.pruneFileName(self.currentExample.dataSource), self.currentExample.dataSource))
        
        self.refresh_ui()

    #--event connections--
    def set_event_connections(self):
        #does not interact with the model
        ui.helpButton.clicked.connect(lambda: webbrowser.open('https://github.com/SamDelaney/LITE/wiki'))
        
        #calling methods from the model
        ui.pasteButton.clicked.connect(lambda: self.retrieve_clipboard())
        ui.copyButton.clicked.connect(lambda: self.copy_to_clipboard())
        ui.AddSourceButton.clicked.connect(lambda: self.get_data_source())

        #language name option radio buttons
        ui.noLangNameButton.clicked.connect(lambda: self.FEOptionsUpdated())
        ui.langNameFirstLineButton.clicked.connect(lambda: self.FEOptionsUpdated())
        ui.langNameOnRightButton.clicked.connect(lambda: self.FEOptionsUpdated())
        #other formatted example options
        ui.ungrammaticalBox.clicked.connect(lambda: self.FEOptionsUpdated())
        ui.litTranslationBox.clicked.connect(lambda: self.FEOptionsUpdated())

        #comboboxes
        ui.dataSourceReferenceBox.clicked.connect(lambda: self.FEOptionsUpdated())
        ui.dataSourceComboBox.activated.connect(lambda: self.FEOptionsUpdated())
        ui.formatStyleComboBox.activated.connect(lambda: self.FEOptionsUpdated())
    

if __name__ ==  "__main__":

    import sys
    app = MainApp(sys.argv)
    LITE = QtWidgets.QMainWindow()
    ui = Ui_LITE()
    ui.setupUi(LITE)
    app.set_event_connections()
    app.initialize_globals()
    app.refresh_ui()
    LITE.show()
    sys.exit(app.exec_())

    
