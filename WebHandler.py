from PSQL import getData
import markdown2

def getWebsite(name) :
    html = getData(name)
    return html
