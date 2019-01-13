from FormattedExample import FormattedExample
from FormatStyle import FormatStyle

def runScript(formattedExample):
    text = "FORMATTED EXAMPLE"
    text += "\n Language Name Option: " + langNameOptionToString(formattedExample)
    text += "\n Include literal translation: " + str(formattedExample.useLiteralTrans)
    text += "\n Indicate as ungrammatical: " + str(formattedExample.isUngrammatical)
    text += "\n Copied Text: \n"
    text += formattedExample.pastedText
    return text

def langNameOptionToString(formattedExample):
    if formattedExample.langNameOption == 0:
        return "0 = 'Do not include language name.'"
    if formattedExample.langNameOption == 1:
        return "1 = 'Include language name as first line.'"
    if formattedExample.langNameOption == 2:
        return "2 = 'Include language name on right.'"