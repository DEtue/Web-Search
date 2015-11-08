import webbrowser

# open default browser and search using given parameters
def searchFor(eng, query):
    webbrowser.open(eng + query, new=2)

# get search engine if anything else besides the 3 choices 
def getEngine(engine):
    goog = "www.google.com/search?q="
    yahoo =  "search.yahoo.com/search?p="
    bing =  "www.bing.com/search?q="
    duck = "https://duckduckgo.com/?q="
    if engine == "google":
        return goog
    elif engine == "yahoo":
        return yahoo
    elif engine == "bing":
        return bing
    elif engine == "duck duck go":
        return duck

