def writeDataToHtml(writeHtmlFileName,data):
	thefile = open(writeHtmlFileName, 'w',encoding='utf-8-sig')
	for item in data:
		print>>thefile, item
	thefile.close()