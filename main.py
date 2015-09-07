import webbrowser

# Choose a search engine
goog = "www.google.com/search?q="
yahoo =  "search.yahoo.com/search?p="
bing =  "www.bing.com/search?q="

engines = [goog, yahoo, bing]

#
def searchFor(eng, query):
    webbrowser.open(eng + query, new=2)

def getEngine(engine):
    if engine == "google":
        return goog
    elif engine == "yahoo":
        return yahoo
    elif engine == "bing":
        return bing

engine = input("Enter Search Engine: ").lower()
query = input("Enter Search Query: ")

searchFor(getEngine(engine), query)
