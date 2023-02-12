# TestDriver
# Used for development
# kb 2-11-2023

import FileReader
import Quote

reader = FileReader.FileReader("../files/quotes.txt")
flatList = reader.openFlatFile()

quoteLister = Quote.QuoteList(flatList)
quotes = quoteLister.tokenize()

print("Listing all quotes...")

for quote in quotes:
    print(quote.sen.strip())
    length = quote.charCount()
    print("Length: ", length)


minWidth = 30
maxWidth = 60


filtered_quotes = quoteLister.filter(minWidth, maxWidth)

print()

print("Listing all quotes meeting criteria: Min(",minWidth,") Max(",maxWidth,")...")

for quote in filtered_quotes:
    print(quote.sen.strip())
    length = quote.charCount()
    print("Length: ", length)


minWidth = 30
maxWidth = 40


filtered_quotes = quoteLister.filter(minWidth, maxWidth)

print()

print("Listing all quotes meeting criteria: Min(",minWidth,") Max(",maxWidth,")...")

for quote in filtered_quotes:
    print(quote.sen.strip())
    length = quote.charCount()
    print("Length: ", length)


