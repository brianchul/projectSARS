def generateDoc1(adviseList):
	global docTitle
	
	adviseContent = readFile("html/advise.html")
	
	for num in range(len(adviseList)):
		adviseContent.append(adviseList[num])
	#或許可以用讀檔的方式避免錯誤roll back
	
	adviseContent[adviseContent.index('@total')] = totalCopies
	for num in range(4):
		adviseContent[adviseContent.index('@g' + str(num))] = grade[num]
	
	for num in range(6):
		for num2 in range(10):
			adviseContent[adviseContent.index('@' + str(num2) + '-' + str(num))] = question[num2+1][num] #without grade
			
	writeDataToHtml("html/adviseTemp.html",adviseContent)
	#os.remove("html/adviseTemp.html")