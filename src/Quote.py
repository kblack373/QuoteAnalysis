# Quote classes 
# Contains the levels of abstraction for a list of quotes, down to each word
# kb 2-11-2023

import re

class QuoteList:
    def __init__(self, flatList):
        self.flat = flatList
        self.ql = []
    
    def tokenize(self):
        flat = self.flat
        ql = []
        for i in flat:
            #remove ALL special characters
            #todo: make this regex a constant
            norm = re.sub("[\.\,\'\"!\[\[\]?&%:;]+", "", i)
            quote = Quote(norm)
            ql.append(quote)
        return ql #will not return this long-term. testing.

class Quote:
    def __init__(self, flatSentence):
        self.sen = flatSentence
        self.tokens = self.sen.split(" ")
#todo: return flat quote content

class Word:
    def __init__(self, flatWord):
        self.raw = flatWord
