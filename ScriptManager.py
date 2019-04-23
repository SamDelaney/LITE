from FormattedExample import FormattedExample
from FormatStyle import FormatStyle
import lxml.etree as ET

#conversion scripts
from scripts.DebugScript import runScript

class ScriptManager:

    def name_option(self, option):
        if option == 0:
            return "none"
        elif option == 1:
            return "first"
        else:
            return "right"

    def convert_text(self, fe):

        doc = ET.parse("scripts/icelandic.flextext")

        xslt = ET.parse("scripts/xml2LeipzigLITE2.xsl")

        transform = ET.XSLT(xslt)


        #Parameters:
        #Include baseline (4-line)
        #pInclude_baseline, 0 or 1
        #Language name
        #pLanguage_name, string
        #Include language name as first line or on right
        #pInclude_language, none, first or right
        #Include data source reference
        #include_source_reference, none, first or right
        #pSource_reference, string (which can have spaces. Eg. (Hayashi, 1997: 67-69)
        #Include literal translation
        #include_literal_trans, 0 or 1
        #Indicate as ungrammatical
        #indicate_ungrammatical, 0 or 1

        newdom = transform(doc,
            pInclude_baseline=ET.XSLT.strparam(str(int(fe.selectedFormatStyle.has_baseline))),
            pLanguage_name=ET.XSLT.strparam(fe.langOption.name), #still need to implement
            pInclude_language=ET.XSLT.strparam(str(self.name_option(fe.langOption.place))),
            pInclude_source_reference=ET.XSLT.strparam(str(self.name_option(fe.dataSource.place))),
            pSource_reference=ET.XSLT.strparam(fe.dataSource.name),
            pInclude_literal_trans=ET.XSLT.strparam(str(int(fe.useLiteralTrans))),
            pIndicate_ungrammatical=ET.XSLT.strparam(str(int(fe.isUngrammatical))),
            pInclude_notes=ET.XSLT.strparam(str(int(fe.includeNotes))))

            #not implemented in XSLT:
            # pIndicate_ungrammatical
            # pInclude_notes

        #return runScript(fe) -testing only
        return ET.tostring(newdom).decode("utf-8")
