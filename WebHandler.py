

def getHTML(url) :
	top = open("top.txt","r")
	bottom = open("bottom.txt", "r")
	data = str(issue_command('SELECT html FROM website.blog WHERE url=\'{}\''.format(url), True)[0])
	content = data[2:-3]
	print(content)
	return str(top.read()) + content + str(bottom.read())