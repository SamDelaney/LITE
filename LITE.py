# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainAppDesign.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LITE(object):
    def setupUi(self, LITE):
        LITE.setObjectName("LITE")
        LITE.resize(525, 654)
        self.centralwidget = QtWidgets.QWidget(LITE)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.formatExample = QtWidgets.QWidget()
        self.formatExample.setObjectName("formatExample")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.formatExample)
        self.verticalLayout.setObjectName("verticalLayout")
        self.PasteButtonLayout = QtWidgets.QHBoxLayout()
        self.PasteButtonLayout.setObjectName("PasteButtonLayout")
        spacerItem = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.PasteButtonLayout.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.PasteButtonLayout.addItem(spacerItem1)
        self.pushButton_2 = QtWidgets.QPushButton(self.formatExample)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.PasteButtonLayout.addWidget(self.pushButton_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.PasteButtonLayout.addItem(spacerItem2)
        self.helpButton = QtWidgets.QPushButton(self.formatExample)
        self.helpButton.setMaximumSize(QtCore.QSize(60, 16777215))
        self.helpButton.setObjectName("helpButton")
        self.PasteButtonLayout.addWidget(self.helpButton)
        self.verticalLayout.addLayout(self.PasteButtonLayout)
        self.PastedTextLayout = QtWidgets.QVBoxLayout()
        self.PastedTextLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.PastedTextLayout.setObjectName("PastedTextLayout")
        self.pastedTextLabel = QtWidgets.QLabel(self.formatExample)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pastedTextLabel.sizePolicy().hasHeightForWidth())
        self.pastedTextLabel.setSizePolicy(sizePolicy)
        self.pastedTextLabel.setMaximumSize(QtCore.QSize(16777215, 10))
        self.pastedTextLabel.setAutoFillBackground(False)
        self.pastedTextLabel.setObjectName("pastedTextLabel")
        self.PastedTextLayout.addWidget(self.pastedTextLabel)
        self.textEdit = QtWidgets.QTextEdit(self.formatExample)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setObjectName("textEdit")
        self.PastedTextLayout.addWidget(self.textEdit)
        self.verticalLayout.addLayout(self.PastedTextLayout)
        self.SelectFormattingLayout = QtWidgets.QHBoxLayout()
        self.SelectFormattingLayout.setObjectName("SelectFormattingLayout")
        self.label = QtWidgets.QLabel(self.formatExample)
        self.label.setObjectName("label")
        self.SelectFormattingLayout.addWidget(self.label)
        self.formatStyleComboBox = QtWidgets.QComboBox(self.formatExample)
        self.formatStyleComboBox.setEditable(False)
        self.formatStyleComboBox.setCurrentText("")
        self.formatStyleComboBox.setObjectName("formatStyleComboBox")
        self.SelectFormattingLayout.addWidget(self.formatStyleComboBox)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.SelectFormattingLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.SelectFormattingLayout)
        self.OptionsLayout = QtWidgets.QVBoxLayout()
        self.OptionsLayout.setObjectName("OptionsLayout")
        self.LanguageNameLayout = QtWidgets.QHBoxLayout()
        self.LanguageNameLayout.setObjectName("LanguageNameLayout")
        self.noLangNameButton = QtWidgets.QRadioButton(self.formatExample)
        self.noLangNameButton.setObjectName("noLangNameButton")
        self.LanguageNameLayout.addWidget(self.noLangNameButton)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.LanguageNameLayout.addItem(spacerItem4)
        self.comboBox = QtWidgets.QComboBox(self.formatExample)
        self.comboBox.setObjectName("comboBox")
        self.LanguageNameLayout.addWidget(self.comboBox)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.LanguageNameLayout.addItem(spacerItem5)
        self.OptionsLayout.addLayout(self.LanguageNameLayout)
        self.langNameFirstLineButton = QtWidgets.QRadioButton(self.formatExample)
        self.langNameFirstLineButton.setObjectName("langNameFirstLineButton")
        self.OptionsLayout.addWidget(self.langNameFirstLineButton)
        self.langNameOnRightButton = QtWidgets.QRadioButton(self.formatExample)
        self.langNameOnRightButton.setObjectName("langNameOnRightButton")
        self.OptionsLayout.addWidget(self.langNameOnRightButton)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.OptionsLayout.addItem(spacerItem6)
        self.DataSourceLayout = QtWidgets.QHBoxLayout()
        self.DataSourceLayout.setObjectName("DataSourceLayout")
        self.dataSourceReferenceBox = QtWidgets.QCheckBox(self.formatExample)
        self.dataSourceReferenceBox.setObjectName("dataSourceReferenceBox")
        self.DataSourceLayout.addWidget(self.dataSourceReferenceBox)
        spacerItem7 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.DataSourceLayout.addItem(spacerItem7)
        self.dataSourceComboBox = QtWidgets.QComboBox(self.formatExample)
        self.dataSourceComboBox.setObjectName("dataSourceComboBox")
        self.DataSourceLayout.addWidget(self.dataSourceComboBox)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.DataSourceLayout.addItem(spacerItem8)
        self.AddSourceLabel = QtWidgets.QLabel(self.formatExample)
        self.AddSourceLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.AddSourceLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.AddSourceLabel.setObjectName("AddSourceLabel")
        self.DataSourceLayout.addWidget(self.AddSourceLabel)
        self.AddSourceButton = QtWidgets.QToolButton(self.formatExample)
        self.AddSourceButton.setObjectName("AddSourceButton")
        self.DataSourceLayout.addWidget(self.AddSourceButton)
        self.OptionsLayout.addLayout(self.DataSourceLayout)
        self.litTranslationBox = QtWidgets.QCheckBox(self.formatExample)
        self.litTranslationBox.setObjectName("litTranslationBox")
        self.OptionsLayout.addWidget(self.litTranslationBox)
        self.ungrammaticalBox = QtWidgets.QCheckBox(self.formatExample)
        self.ungrammaticalBox.setObjectName("ungrammaticalBox")
        self.OptionsLayout.addWidget(self.ungrammaticalBox)
        self.TextPreviewLayout = QtWidgets.QVBoxLayout()
        self.TextPreviewLayout.setObjectName("TextPreviewLayout")
        self.OutputPreviewLabel = QtWidgets.QLabel(self.formatExample)
        self.OutputPreviewLabel.setObjectName("OutputPreviewLabel")
        self.TextPreviewLayout.addWidget(self.OutputPreviewLabel)
        self.OutputPreviewTextEdit = QtWidgets.QTextEdit(self.formatExample)
        self.OutputPreviewTextEdit.setObjectName("OutputPreviewTextEdit")
        self.TextPreviewLayout.addWidget(self.OutputPreviewTextEdit)
        self.OptionsLayout.addLayout(self.TextPreviewLayout)
        self.verticalLayout.addLayout(self.OptionsLayout)
        self.OutputTypeLayout = QtWidgets.QHBoxLayout()
        self.OutputTypeLayout.setObjectName("OutputTypeLayout")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.OutputTypeLayout.addItem(spacerItem9)
        self.OutputSelectionLabel = QtWidgets.QLabel(self.formatExample)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.OutputSelectionLabel.setFont(font)
        self.OutputSelectionLabel.setObjectName("OutputSelectionLabel")
        self.OutputTypeLayout.addWidget(self.OutputSelectionLabel)
        self.comboBox_3 = QtWidgets.QComboBox(self.formatExample)
        self.comboBox_3.setObjectName("comboBox_3")
        self.OutputTypeLayout.addWidget(self.comboBox_3)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.OutputTypeLayout.addItem(spacerItem10)
        self.verticalLayout.addLayout(self.OutputTypeLayout)
        self.CopyButtonLayout = QtWidgets.QHBoxLayout()
        self.CopyButtonLayout.setObjectName("CopyButtonLayout")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.CopyButtonLayout.addItem(spacerItem11)
        self.CopyButton = QtWidgets.QPushButton(self.formatExample)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CopyButton.sizePolicy().hasHeightForWidth())
        self.CopyButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.CopyButton.setFont(font)
        self.CopyButton.setObjectName("CopyButton")
        self.CopyButtonLayout.addWidget(self.CopyButton)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.CopyButtonLayout.addItem(spacerItem12)
        self.verticalLayout.addLayout(self.CopyButtonLayout)
        self.tabWidget.addTab(self.formatExample, "")
        self.formatStyle = QtWidgets.QWidget()
        self.formatStyle.setObjectName("formatStyle")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.formatStyle)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.styleNameLayout = QtWidgets.QHBoxLayout()
        self.styleNameLayout.setObjectName("styleNameLayout")
        self.styleNameLabel = QtWidgets.QLabel(self.formatStyle)
        self.styleNameLabel.setObjectName("styleNameLabel")
        self.styleNameLayout.addWidget(self.styleNameLabel, 0, QtCore.Qt.AlignRight)
        self.styleNameComboBox = QtWidgets.QComboBox(self.formatStyle)
        self.styleNameComboBox.setObjectName("styleNameComboBox")
        self.styleNameLayout.addWidget(self.styleNameComboBox, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_2.addLayout(self.styleNameLayout)
        self.bodyLayout = QtWidgets.QFormLayout()
        self.bodyLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldsStayAtSizeHint)
        self.bodyLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.bodyLayout.setFormAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.bodyLayout.setObjectName("bodyLayout")
        self.lineListWidget = QtWidgets.QListWidget(self.formatStyle)
        self.lineListWidget.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineListWidget.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.lineListWidget.setObjectName("lineListWidget")
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Checked)
        self.lineListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Checked)
        self.lineListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Checked)
        self.lineListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Checked)
        self.lineListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Checked)
        self.lineListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Checked)
        self.lineListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Checked)
        self.lineListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.lineListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Checked)
        self.lineListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Checked)
        self.lineListWidget.addItem(item)
        self.bodyLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lineListWidget)
        self.linePropsLayout = QtWidgets.QVBoxLayout()
        self.linePropsLayout.setContentsMargins(-1, -1, -1, 6)
        self.linePropsLayout.setObjectName("linePropsLayout")
        self.linePropsLabel = QtWidgets.QLabel(self.formatStyle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.linePropsLabel.sizePolicy().hasHeightForWidth())
        self.linePropsLabel.setSizePolicy(sizePolicy)
        self.linePropsLabel.setMinimumSize(QtCore.QSize(0, 12))
        self.linePropsLabel.setObjectName("linePropsLabel")
        self.linePropsLayout.addWidget(self.linePropsLabel, 0, QtCore.Qt.AlignHCenter)
        self.linePropsInternalLayout = QtWidgets.QFormLayout()
        self.linePropsInternalLayout.setObjectName("linePropsInternalLayout")
        self.legendLabelLabel = QtWidgets.QLabel(self.formatStyle)
        self.legendLabelLabel.setObjectName("legendLabelLabel")
        self.linePropsInternalLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.legendLabelLabel)
        self.legendLabelLineEdit = QtWidgets.QLineEdit(self.formatStyle)
        self.legendLabelLineEdit.setObjectName("legendLabelLineEdit")
        self.linePropsInternalLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.legendLabelLineEdit)
        self.fontSizeLabel = QtWidgets.QLabel(self.formatStyle)
        self.fontSizeLabel.setObjectName("fontSizeLabel")
        self.linePropsInternalLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.fontSizeLabel)
        self.fontSizeLayout = QtWidgets.QHBoxLayout()
        self.fontSizeLayout.setObjectName("fontSizeLayout")
        self.fontSizeLineEdit = QtWidgets.QLineEdit(self.formatStyle)
        self.fontSizeLineEdit.setObjectName("fontSizeLineEdit")
        self.fontSizeLayout.addWidget(self.fontSizeLineEdit)
        self.fontSizeComboBox = QtWidgets.QComboBox(self.formatStyle)
        self.fontSizeComboBox.setObjectName("fontSizeComboBox")
        self.fontSizeLayout.addWidget(self.fontSizeComboBox)
        self.linePropsInternalLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.fontSizeLayout)
        self.fontStyleLabel = QtWidgets.QLabel(self.formatStyle)
        self.fontStyleLabel.setObjectName("fontStyleLabel")
        self.linePropsInternalLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.fontStyleLabel)
        self.fontStyleLayout = QtWidgets.QHBoxLayout()
        self.fontStyleLayout.setObjectName("fontStyleLayout")
        self.comboBox_4 = QtWidgets.QComboBox(self.formatStyle)
        self.comboBox_4.setObjectName("comboBox_4")
        self.fontStyleLayout.addWidget(self.comboBox_4)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.fontStyleLayout.addItem(spacerItem13)
        self.linePropsInternalLayout.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.fontStyleLayout)
        self.linePropsLayout.addLayout(self.linePropsInternalLayout)
        self.removeSpacesCheckBox = QtWidgets.QCheckBox(self.formatStyle)
        self.removeSpacesCheckBox.setObjectName("removeSpacesCheckBox")
        self.linePropsLayout.addWidget(self.removeSpacesCheckBox)
        self.bodyLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.linePropsLayout)
        self.maxWidthLabel = QtWidgets.QLabel(self.formatStyle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maxWidthLabel.sizePolicy().hasHeightForWidth())
        self.maxWidthLabel.setSizePolicy(sizePolicy)
        self.maxWidthLabel.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.maxWidthLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.maxWidthLabel.setObjectName("maxWidthLabel")
        self.bodyLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.maxWidthLabel)
        self.maxWidthLayout = QtWidgets.QHBoxLayout()
        self.maxWidthLayout.setObjectName("maxWidthLayout")
        self.maxWidthLineEdit = QtWidgets.QLineEdit(self.formatStyle)
        self.maxWidthLineEdit.setMaximumSize(QtCore.QSize(133, 16777215))
        self.maxWidthLineEdit.setAutoFillBackground(False)
        self.maxWidthLineEdit.setClearButtonEnabled(False)
        self.maxWidthLineEdit.setObjectName("maxWidthLineEdit")
        self.maxWidthLayout.addWidget(self.maxWidthLineEdit)
        self.maxWidthComboBox = QtWidgets.QComboBox(self.formatStyle)
        self.maxWidthComboBox.setObjectName("maxWidthComboBox")
        self.maxWidthLayout.addWidget(self.maxWidthComboBox)
        self.bodyLayout.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.maxWidthLayout)
        self.numberedExampleLabel = QtWidgets.QLabel(self.formatStyle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.numberedExampleLabel.sizePolicy().hasHeightForWidth())
        self.numberedExampleLabel.setSizePolicy(sizePolicy)
        self.numberedExampleLabel.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.numberedExampleLabel.setObjectName("numberedExampleLabel")
        self.bodyLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.numberedExampleLabel)
        self.firstLineLabel = QtWidgets.QLabel(self.formatStyle)
        self.firstLineLabel.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.firstLineLabel.setObjectName("firstLineLabel")
        self.bodyLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.firstLineLabel)
        self.subseqLinesLabel = QtWidgets.QLabel(self.formatStyle)
        self.subseqLinesLabel.setObjectName("subseqLinesLabel")
        self.bodyLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.subseqLinesLabel)
        self.numberedExampleLineEdit = QtWidgets.QLineEdit(self.formatStyle)
        self.numberedExampleLineEdit.setObjectName("numberedExampleLineEdit")
        self.bodyLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.numberedExampleLineEdit)
        self.firstLineLineEdit = QtWidgets.QLineEdit(self.formatStyle)
        self.firstLineLineEdit.setObjectName("firstLineLineEdit")
        self.bodyLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.firstLineLineEdit)
        self.subseqLinesLineEdit = QtWidgets.QLineEdit(self.formatStyle)
        self.subseqLinesLineEdit.setObjectName("subseqLinesLineEdit")
        self.bodyLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.subseqLinesLineEdit)
        self.formatForLabel = QtWidgets.QLabel(self.formatStyle)
        self.formatForLabel.setObjectName("formatForLabel")
        self.bodyLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.formatForLabel)
        self.formatForComboBox = QtWidgets.QComboBox(self.formatStyle)
        self.formatForComboBox.setObjectName("formatForComboBox")
        self.bodyLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.formatForComboBox)
        self.verticalLayout_2.addLayout(self.bodyLayout)
        self.stylePreviewLabel = QtWidgets.QLabel(self.formatStyle)
        self.stylePreviewLabel.setObjectName("stylePreviewLabel")
        self.verticalLayout_2.addWidget(self.stylePreviewLabel)
        self.stylePreviewBrowser = QtWidgets.QTextBrowser(self.formatStyle)
        self.stylePreviewBrowser.setObjectName("stylePreviewBrowser")
        self.verticalLayout_2.addWidget(self.stylePreviewBrowser)
        self.saveButtonsLayout = QtWidgets.QHBoxLayout()
        self.saveButtonsLayout.setObjectName("saveButtonsLayout")
        self.saveButton = QtWidgets.QPushButton(self.formatStyle)
        self.saveButton.setObjectName("saveButton")
        self.saveButtonsLayout.addWidget(self.saveButton, 0, QtCore.Qt.AlignRight)
        self.saveAsButton = QtWidgets.QPushButton(self.formatStyle)
        self.saveAsButton.setObjectName("saveAsButton")
        self.saveButtonsLayout.addWidget(self.saveAsButton, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_2.addLayout(self.saveButtonsLayout)
        self.tabWidget.addTab(self.formatStyle, "")
        self.outputFormats = QtWidgets.QWidget()
        self.outputFormats.setObjectName("outputFormats")
        self.tabWidget.addTab(self.outputFormats, "")
        self.preferences = QtWidgets.QWidget()
        self.preferences.setObjectName("preferences")
        self.tabWidget.addTab(self.preferences, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        LITE.setCentralWidget(self.centralwidget)

        self.retranslateUi(LITE)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(LITE)

    def retranslateUi(self, LITE):
        _translate = QtCore.QCoreApplication.translate
        LITE.setWindowTitle(_translate("LITE", "Linguistic Interlinear Text Exampler"))
        self.pushButton_2.setText(_translate("LITE", "Paste FieldWorks Text Segment from clipboard"))
        self.helpButton.setText(_translate("LITE", "Help"))
        self.pastedTextLabel.setText(_translate("LITE", "Pasted Fieldworks Text Segment"))
        self.label.setText(_translate("LITE", "TextLabel"))
        self.noLangNameButton.setText(_translate("LITE", "Do not include language name"))
        self.langNameFirstLineButton.setText(_translate("LITE", "Include language name as first line"))
        self.langNameOnRightButton.setText(_translate("LITE", "Include language name on right"))
        self.dataSourceReferenceBox.setText(_translate("LITE", "Include data source reference"))
        self.AddSourceLabel.setText(_translate("LITE", "Add data source:"))
        self.AddSourceButton.setText(_translate("LITE", "..."))
        self.litTranslationBox.setText(_translate("LITE", "Include literal translation"))
        self.ungrammaticalBox.setText(_translate("LITE", "Indicate as ungrammatical"))
        self.OutputPreviewLabel.setText(_translate("LITE", "Output preview:"))
        self.OutputSelectionLabel.setText(_translate("LITE", "Output as: "))
        self.CopyButton.setText(_translate("LITE", "    Copy formatted example to clipboard    "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.formatExample), _translate("LITE", "Create formatted example"))
        self.styleNameLabel.setText(_translate("LITE", "LITE style name: "))
        __sortingEnabled = self.lineListWidget.isSortingEnabled()
        self.lineListWidget.setSortingEnabled(False)
        item = self.lineListWidget.item(0)
        item.setText(_translate("LITE", "Word"))
        item = self.lineListWidget.item(1)
        item.setText(_translate("LITE", "Morphemes"))
        item = self.lineListWidget.item(2)
        item.setText(_translate("LITE", "Lex. Entries"))
        item = self.lineListWidget.item(3)
        item.setText(_translate("LITE", "Lex. Gloss"))
        item = self.lineListWidget.item(4)
        item.setText(_translate("LITE", "Lex. Gram. Info."))
        item = self.lineListWidget.item(5)
        item.setText(_translate("LITE", "Word Gloss"))
        item = self.lineListWidget.item(6)
        item.setText(_translate("LITE", "Word Cat."))
        item = self.lineListWidget.item(7)
        item.setText(_translate("LITE", "Free Translation"))
        item = self.lineListWidget.item(8)
        item.setText(_translate("LITE", "Literal Translation"))
        item = self.lineListWidget.item(9)
        item.setText(_translate("LITE", "Note"))
        self.lineListWidget.setSortingEnabled(__sortingEnabled)
        self.linePropsLabel.setText(_translate("LITE", "Edit Line Properties"))
        self.legendLabelLabel.setText(_translate("LITE", "Legend label: "))
        self.fontSizeLabel.setText(_translate("LITE", "Font size: "))
        self.fontStyleLabel.setText(_translate("LITE", "Font style: "))
        self.removeSpacesCheckBox.setText(_translate("LITE", "Remove spaces between morphemes on polymorphemic words"))
        self.maxWidthLabel.setText(_translate("LITE", "Maximum width of example: "))
        self.numberedExampleLabel.setText(_translate("LITE", "Numbered Example stylename: "))
        self.firstLineLabel.setText(_translate("LITE", "First line stylename: "))
        self.subseqLinesLabel.setText(_translate("LITE", "Subsequent lines stylename: "))
        self.formatForLabel.setText(_translate("LITE", "Format for: "))
        self.stylePreviewLabel.setText(_translate("LITE", "Preview:"))
        self.saveButton.setText(_translate("LITE", "Save"))
        self.saveAsButton.setText(_translate("LITE", "Save As ..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.formatStyle), _translate("LITE", "Create format styles"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.outputFormats), _translate("LITE", "Create output formats"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.preferences), _translate("LITE", "Preferences"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LITE = QtWidgets.QMainWindow()
    ui = Ui_LITE()
    ui.setupUi(LITE)
    LITE.show()
    sys.exit(app.exec_())

