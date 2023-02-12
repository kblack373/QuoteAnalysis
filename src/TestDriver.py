# TestDriver
# Used for development
# kb 2-11-2023

import FileReader
import Quote

reader = FileReader.FileReader("../files/quotes.txt")
flatList = reader.openFlatFile()

quoteLister = Quote.QuoteList(flatList)
quotes = quoteLister.tokenize()

for quote in quotes:
    print(quote.sen)
    length = quote.charCount()
    print("Length: ", length)

