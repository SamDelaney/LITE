from FormatStyle import FormatStyle
from dataclasses import dataclass

class FormattedExample:
    @dataclass
    class DisplayOption:
        name: str
        place: int #0 = none, 1 = first line, 2 = right side
        ref: str = ""

    selectedFormatStyle = FormatStyle("3-line GSRL standard", False)

    langOption = DisplayOption("", 0)
    dataSource = DisplayOption("", 0)

    useLiteralTrans = False
    isUngrammatical = False
    includeNotes = False

    pastedText = ""
    outputText = pastedText

    def __init__(self, text, formatStyle):
        pastedText = text
        selectedFormatStyle = formatStyle
