# FileReader Object
# Reads in a flat text file, returns line by line
# ideally, this class will be expanded to read in other file types and sanitize input
# for now, it assumes that the file read in is just a list of quotes, delimited by line-breaks.
# kb 2-11-2023

class FileReader:

    #self.filename = ''

    def __init__(self, filename):
        self.filename = filename
        self.delimiter = ','

    def openFlatFile(self):
        #returns a basic list containing lines in file
        filename=self.filename

        file = open(filename, "r")
        #initiate list 
        lineList = []

        for line in file:
            lineList.append(line)
        
        file.close()
        return lineList
 
