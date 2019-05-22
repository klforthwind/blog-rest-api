from PSQL import issue_command

def getHTML(url) :
	return issue_command('SELECT * FROM website.blog WHERE url=\'{}\''.format(url), True);