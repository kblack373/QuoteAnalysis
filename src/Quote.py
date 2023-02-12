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
        return ql 

class Quote:
    def __init__(self, flatSentence):
        self.sen = flatSentence
        self.charCount = len(self.sen.strip())
        self.tokens  = self.sen.split(" ") 
        self.wordmount = len(self.tokens)

    def __str__(self):
        return f"{self.sen}"
    def getRaw(self):
        return(self.sen)
    
    def atomize(self, words):
        wl = []
        for word in words:
            wl.append(word)


class Word:
    def __init__(self, flatWord):
        self.raw = flatWord
