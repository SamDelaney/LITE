from FormattedExample import FormattedExample
from FormatStyle import FormatStyle
import lxml.etree as ET

#conversion scripts
from scripts.DebugScript import runScript

class ScriptManager:

    def convert_text(self, fe):
        #temporary code, testing xsl development

        doc = ET.parse("scripts/icelandic.flextext")
        
        if(fe.selectedFormatStyle.stylename == "3-line GSRL standard"):
            xslt = ET.parse("scripts/xml2htm.xsl")
        else:
            xslt = ET.parse("scripts/xml2Leipzig.xsl")
            
        transform = ET.XSLT(xslt)
        newdom = transform(doc)
        print(ET.tostring(newdom, pretty_print=True))

        #return runScript(fe)
        return ET.tostring(newdom).decode("utf-8")
