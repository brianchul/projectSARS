def writeDataToHtml(writeHtmlFileName,data):
	thefile = open(writeHtmlFileName, 'w')
	for item in data:
		print>>thefile, item
	thefile.close()