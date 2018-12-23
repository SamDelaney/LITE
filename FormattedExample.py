from FormatStyle import FormatStyle

class FormattedExample:
    selectedFormatStyle = FormatStyle("3-line GSRL standard")
    pastedText = ""
    
    def __init__(self, text, formatStyle):
        pastedText = text
        selectedFormatStyle = formatStyle
