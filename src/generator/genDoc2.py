def generateDoc2():
	quantifyContent = readFile("html/quantify.html")
	quantifyAdvise = readFile("html/quantifyAdvise.txt")
	quantifyData = calculateQuantifyData()
	print "making bar chart..."
	makeBarChart(quantifyData)
	quantifyTotalScore = ""
	quantifyTotalScoreSum = 0
	
	for num in range(10):
	
		if quantifyData[num] > 5.5:
			quantifyAdviseTemp = quantifyAdvise[num*3]
		elif quantifyData[num] < 5.6 and quantifyData[num] > 4.5:
			quantifyAdviseTemp = quantifyAdvise[num*3+1]
		elif quantifyData[num] < 4.6:
			quantifyAdviseTemp = quantifyAdvise[num*3+2]
			
		quantifyContent[quantifyContent.index("@" + str(num) + "-0" )] = quantifyData[num]
		quantifyContent[quantifyContent.index("@" + str(num) + "-1" )] = round(quantifyData[num]/10,2)
		quantifyContent[quantifyContent.index("@" + str(num) + "-2" )] = quantifyAdviseTemp
		
		quantifyTotalScore = quantifyTotalScore +  str(round(quantifyData[num]/10,2)) + "+"
		quantifyTotalScoreSum = quantifyTotalScoreSum + round(quantifyData[num]/10,2)
		
		
	quantifyContent[quantifyContent.index("@10-0")] = str(quantifyTotalScore[:-1]) + "=" + str(quantifyTotalScoreSum)
	quantifyContent[quantifyContent.index("@10-1")] = str(quantifyTotalScoreSum) + "/6=" + str(round(quantifyTotalScoreSum/6,2)*100) + "%"
	quantifyContent[quantifyContent.index("@10-2")] = docTitle.encode('big5')
	writeDataToHtml("html/quantifyTemp.html",quantifyContent)
	convertHtmlToDoc("html/quantifyTemp.html", docTitle + "quantify")
	os.remove("html/quantifyTemp.html")