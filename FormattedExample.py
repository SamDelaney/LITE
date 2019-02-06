from FormatStyle import FormatStyle

class FormattedExample:
    selectedFormatStyle = FormatStyle("3-line GSRL standard")
    langNameOption = 0
    useLiteralTrans = False
    isUngrammatical = False
    pastedText = ""
    dataSource = ""
    dataSourceRef = ""
    
    def __init__(self, text, formatStyle):
        pastedText = text
        selectedFormatStyle = formatStyle
