from PyQt5 import QtCore, QtGui, QtWidgets
from LITE_UI import Ui_LITE
from LITE_Helpers import TextHelper, PutHtml, paste_win32
#from ExampleDisplayWidget import Ui_ExampleWidget
from FormatStyle import FormatStyle
from FormattedExample import FormattedExample
from ScriptManager import ScriptManager
import clipboard
import webbrowser
import time
import pickle
import sys

class AutoSetup_Ui_LITE(Ui_LITE):
    def __init__(self):
        Ui_LITE.__init__(self)

    def setupUi(self, LITE):
        Ui_LITE.setupUi(self, LITE)

        self.langButtons = QtWidgets.QButtonGroup(None)
        self.sourceRefButtons = QtWidgets.QButtonGroup(None)

        self.langButtons.addButton(self.noLangNameButton, 0)
        self.langButtons.addButton(self.langNameFirstLineButton, 1)
        self.langButtons.addButton(self.langNameOnRightButton, 2)

        self.sourceRefButtons.addButton(self.noDataSourceButton, 0)
        self.sourceRefButtons.addButton(self.dataSourceFirstLineButton, 1)
        self.sourceRefButtons.addButton(self.dataSourceOnRightButton, 2)


class MainApp(QtWidgets.QApplication):
    formatStyles = [] #array of FormatStyle
    dataSources = [] #array of tuples of (pruned file name, full path)
    exampleHistory = [] #array of FormattedExample, updated on Copy to Clipboard
    sm = ScriptManager()
    currentExample = FormattedExample("", FormatStyle("", False)) #initialized with empty values

    def __init__(self, arg):
        QtWidgets.QApplication.__init__(self, arg)


    #--helper methods--
    def store_data(self):
        data = [self.formatStyles, self.dataSources, self.exampleHistory, self.currentExample]
        with open('data/LITE_data.pickle', 'wb') as handle:
            pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)


    def initialize_globals(self):
        #ui.exampleListView.setModel(Ui_ExampleWidget()) #incomplete, commented out intentionally

        #retrieves data from pickle file
        try:
            with open('data/LITE_data.pickle', 'rb') as handle:
               data = pickle.load(handle)
            self.formatStyles = data[0]
            self.dataSources = data[1]
            self.exampleHistory = data[2]
            self.currentExample = data[3]
        except:
            #initialize default format styles
            self.formatStyles.append(FormatStyle("3-line GSRL standard", False))
            self.formatStyles.append(FormatStyle("4-line GSRL standard", True))

        #set the checked radio buttons
        ui.langButtons.button(self.currentExample.langOption.place).setChecked(True)
        ui.sourceRefButtons.button(self.currentExample.dataSource.place).setChecked(True)

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
                ui.dataSourceComboBox.findText(TextHelper.pruneFileName(self.currentExample.dataSource.ref))) #set index to selected item
            ui.clipboardContentTextEdit.setText(self.currentExample.pastedText)

        if self.currentExample.dataSource.ref == "":
            global errormessagedialog #Must be global to persist after the function completes. This is bad practice, and will be changed before final version.
            errormessagedialog = QtWidgets.QErrorMessage()
            errormessagedialog.showMessage('Please select a data source.')

        elif self.currentExample.pastedText == "":
            return

        else:
            ui.clipboardContentTextEdit.setText(self.currentExample.pastedText)
            #clear, convert and preview output text
            ui.outputPreviewTextEdit.clear()
            self.currentExample.outputText = self.sm.convert_text(self.currentExample)
            ui.outputPreviewTextEdit.insertHtml(self.currentExample.outputText)

    #--user actions--
    def FEOptionsUpdated(self):
        #language name option radio buttons
        self.currentExample.langOption.place = ui.langButtons.checkedId()

        #data source reference option radio buttons
        self.currentExample.dataSource.place = ui.sourceRefButtons.checkedId()

        #other formatted example options
        self.currentExample.isUngrammatical = ui.ungrammaticalBox.isChecked()
        self.currentExample.useLiteralTrans = ui.litTranslationBox.isChecked()

        self.currentExample.dataSource.name = str(ui.dataSourceNameComboBox.currentText())
        self.currentExample.langOption.name = str(ui.languageNameComboBox.currentText())

        #format style combobox
        self.currentExample.selectedFormatStyle = next((fs for fs in self.formatStyles if fs.stylename == ui.formatStyleComboBox.currentText()), None)

        #data source combobox
        if len(self.dataSources) > 0:
            self.currentExample.dataSource.ref = self.dataSources[ui.dataSourceComboBox.currentIndex()][1]

        self.refresh_ui()

    def retrieve_clipboard(self):

        self.currentExample.pastedText = paste_win32()

        self.sm.SetPhrase(self.currentExample)

        self.refresh_ui()

    def copy_to_clipboard(self):
        #outputs into the html portion of the clipboard
        PutHtml(self.currentExample.outputText)

        #gets time since epoch (time()) and translates it into current time (ctime())
        ui.updateTimeLabel.setText("Last Updated: " + time.ctime(time.time()))

        #adds current formatted example to history
        self.exampleHistory.append(self.currentExample)
        self.store_data()

    def get_data_source(self):
        self.currentExample.dataSource.ref, _ = QtWidgets.QFileDialog.getOpenFileName(ui.AddSourceButton, 'Get Data Source', '', 'Flextext files (*.flextext)')
        self.dataSources.append((TextHelper.pruneFileName(self.currentExample.dataSource.ref), self.currentExample.dataSource.ref))
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
        #language name option radio buttons
        ui.noDataSourceButton.clicked.connect(lambda: self.FEOptionsUpdated())
        ui.dataSourceFirstLineButton.clicked.connect(lambda: self.FEOptionsUpdated())
        ui.dataSourceOnRightButton.clicked.connect(lambda: self.FEOptionsUpdated())
        #other formatted example options
        ui.ungrammaticalBox.clicked.connect(lambda: self.FEOptionsUpdated())
        ui.litTranslationBox.clicked.connect(lambda: self.FEOptionsUpdated())
        ui.includeNotesBox.clicked.connect(lambda: self.FEOptionsUpdated())

        #comboboxes
        ui.dataSourceNameComboBox.activated.connect(lambda: self.FEOptionsUpdated())
        ui.dataSourceComboBox.activated.connect(lambda: self.FEOptionsUpdated())
        ui.formatStyleComboBox.activated.connect(lambda: self.FEOptionsUpdated())


if __name__ ==  "__main__":

    import sys
    app = MainApp(sys.argv)
    LITE = QtWidgets.QMainWindow()
    ui = AutoSetup_Ui_LITE()
    ui.setupUi(LITE)
    app.set_event_connections()
    app.initialize_globals()
    app.refresh_ui()
    LITE.show()
    sys.exit(app.exec_())
