# Quote classes 
# Contains the levels of abstraction for a list of quotes, down to each word
# kb 2-11-2023

import re

#declare constants
re_spec = "[\.\,\'\"!\[\[\]?&%:;]+"

class QuoteList:
    def __init__(self, flatList):
        self.flat = flatList
        self.ql = []
    
    def tokenize(self):
        flat = self.flat
        ql = []
        for i in flat:
            #remove ALL special characters
            norm = re.sub(re_spec, "", i)
            quote = Quote(norm)
            ql.append(quote)
            #pass in local ql to global ql
            self.ql = ql
        return ql
    
    def getList(self):
        return self.ql

    def filter(self, minWidth, maxWidth, height):
        if height == 0:
            return None
        ql = self.ql
        qlFil = []

        for quote in ql:
            lineLen = quote.charCount
            #divide the line char count by number of lines
            lineLen = lineLen/height
            if maxWidth>=lineLen and minWidth<lineLen:
                qlFil.append(quote)
        return qlFil

    def filter(self, minWidth, maxWidth):
        ql = self.ql
        qlFil = []
        
        for quote in ql:
            lineLen = quote.charCount()
            if maxWidth>=lineLen and minWidth<=lineLen:
                qlFil.append(quote)
        return qlFil

class Quote:
    def __init__(self, flatSentence):
        self.sen = flatSentence.strip()
        self.countSpace = False
        self.tokens  = self.sen.split(" ") 

    def __str__(self):
        return f"{self.sen}"
    
    def getRaw(self):
        #just the raw sentence
        return(self.sen)
    
    def charCount(self):
        if self.countSpace:
             return len(self.sen)
        else:
             return len(self.sen.replace(" ",""))

    def wordCount(self):
        return len(self.tokens)
    
    def toggleCountSpace(self):
    #toggles whether to count spaces, then returns the current setting
        if self.countSpace:
            self.countSpace = False
        else:
            self.countSpace = True

        return self.countSpace

    def atomize(self, words):
        wl = []
        for word in words:
            wl.append(word)


class Word:
    def __init__(self, flatWord):
        self.raw = flatWord
