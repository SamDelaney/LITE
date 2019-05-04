import lxml.etree as ET
from LITE_Helpers import SequenceMatcher

class PhraseFinder:

    def __init__(self, path):
        self.FlextextSource = ET.parse(path)
        self.Phrases = []
        self.headers = {"wordtxt" : "Word"
                ,"morphtxt" : "Morphemes"
                , "morphcf" : "Lex.Entries" #spaces removed before referenced
                , "morphgls" : "Lex.Gloss"
                , "morphmsa" : "Lex.Gram.Info"
                , "wordgls" : "WordGloss"
                , "wordpos" : "WordCat."
                , "phrasegls" : "Free"
                , "phraselit" : "Lit."}

        #returns complete flextext file for target paragraph
    def Phrase(self, clipboard):
        self.lines = clipboard.split("\n")
        output = self.GetHead()
        output += ET.tostring(self.GetMatch(clipboard)).decode("utf-8")
        output += self.GetTail()

        #print(output)
        #output = ""
        #for line in lines:
        #    output += str(line) + "\n"

        return output

        #guid is only unique part of this text, and not involved in
    def GetHead(self):
        return """<?xml version="1.0" encoding="utf-8"?>
        <document version="2">
        <interlinear-text guid="dcca1a8a-95bf-4814-897e-6587e7a2e75d">
        <paragraphs>
        <paragraph>"""

    def GetTail(self):
        return """</paragraph>
        </paragraphs>
        </interlinear-text>
        </document>"""

        #returns the <phrase> element most matching the clipboard content
    def GetMatch(self, clipboard):

        self.GetPhrases()
        if len(self.Phrases) == 1:
            return self.Phrases

        self.ParseByIndex(clipboard)
        if len(self.Phrases) == 1:
            return self.Phrases

        return self.ParseByContent(clipboard)

        #get all paragraph elements and add them to self.Phrases
    def GetPhrases(self):
        self.Phrases = self.FlextextSource.findall(".//phrase")
        #print(len(self.Phrases))

        #remove all paragraph elements that do not match the paragraph number
        # unless no such match exists
    def ParseByIndex(self, input):
        #get index for input
        try:
            #print("Segment Number: " + self.lines[0].split("\t")[0])
            num = float(self.lines[0].split("\t")[0])
            self.lines.pop(0) #remove index from clipboard for editing clarity
        except:
            return

        #get paragraphs which do not match input index
        ToRemove = []
        for i in range(len(self.Phrases)):
            paranum = None
            #get paragraph segment number
            for item in self.Phrases[i].iter('item'):
                if item.attrib['type'] == "segnum":
                    paranum = item.text
                    break

            #compare segment number to input index
            if paranum == None:
                return
            if float(paranum) != num:
                ToRemove.append(self.Phrases[i])

        #remove all non-matching paragraphs
        if len(ToRemove) < len(self.Phrases):
            for item in ToRemove:
                self.Phrases.remove(item)



        #return closest match to input
        #perhaps modify to return list of paragraphs in future?
    def ParseByContent(self, input):
        highScore = (-1, -1) #phrase number, score
        #print(len(self.Phrases))
        for i in range(len(self.Phrases)):
            phrase = {} #creates dictionary for paragraph lines
            for item in self.Phrases[i].iter('item'): #fill dictionary with lines
                if item.attrib['type'] in phrase.keys():
                    phrase[item.attrib['type']] += str(item.text) #add to value at key if key exists
                else:
                    phrase[item.attrib['type']] = str(item.text) #create key + value if key doesn't exist


            currentScore = self.GetLineScore(input, phrase)

            if currentScore > highScore[1]:
                highScore = (i, currentScore)
                #print(highScore)
            #end for
        #end for
        return self.Phrases[highScore[0]]
    #end def

    def GetLineScore(self, input, phrase):
        currentScore = 0.0
        lines = self.formatInput(input)
        for line in lines:
            for xmlLine in phrase.values():
                currentScore += SequenceMatcher(None, xmlLine, line).ratio()

            #end for
        #end for
        return currentScore
    #end def

    def formatInput(self, input):
        output = []
        for line in input.split("\n"):
            #formatting line to match content of paragraph{}
            #segment num removed in ParseByIndex()
            line.replace(" ","") #remove spaces
            words = line.split("\t") #remove tabs and split
            if len(words) > 1:
                words[1] = ''.join(words[1].split()) #remove weird whitespace from headers
                #print(words[1])
                if words[1] in self.headers.values():#remove header column
                    words.pop(1)
            line = "".join(words) #rejoin
            line.strip() #remove whitespace on ends
            output.append(line)
        return output


#testing
#PF = PhraseFinder(r"C:\Users\Sam\LITE\scripts\FullTuwaliIfugaoProj.flextext")
#PF.GetPhrases()
#print(ET.tostring(PF.ParseByContent("	Word	Hay	pundallanan		ina	di	mangipaatun			hiya	.")))
