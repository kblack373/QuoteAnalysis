# TestDriver
# Used for development
# kb 2-11-2023

import FileReader
import Quote

reader = FileReader.FileReader("../files/tester.csv")
flatList = reader.openFlatFile()

ql = Quote.QuoteList(flatList)
print(ql.tokenize())
