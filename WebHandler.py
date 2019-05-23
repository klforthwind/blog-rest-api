import markdown2

def getHTML(url) :
	top = open("top.txt","r")
	bottom = open("bottom.txt", "r")
	fileLoc = str(url) + ".md"
	data = open(fileLoc, "r")
	content = markdown2.markdown(data.read())
	return str(top.read()) + content + str(bottom.read())