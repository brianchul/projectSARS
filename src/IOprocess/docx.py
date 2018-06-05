def convertHtmlToDoc(htmlName,docName):
	docName = "output/" + docName + ".doc"
	word = win32com.client.Dispatch("Word.Application")

	in_file  = os.path.abspath(htmlName)
	out_file = os.path.abspath(docName)

	# Open and copy HTML
	doc = word.Documents.Add(in_file)
	word.Selection.WholeStory()
	word.Selection.Copy()
	doc.Close()

	# Open new document, paste HTML and save
	doc = word.Documents.Add()
	word.Selection.Paste()
	doc.SaveAs(out_file, FileFormat=1)
	doc.Close()
	
	word.Quit()