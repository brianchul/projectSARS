def generateDoc3():
	qualityContent = readFile("./html/quality.html")
	qualityPieTitle = [u'1.整體評價',u'2. 事前宣傳',u'3. 場地',u'4. 講師上課流暢度',u'5. 講師的上課速度',u'6.講師表達清晰度',u'7. 主題和內容的契合度',u'8. 內容理解程度',u'9.主題和內容契合度',u'10.內容吸引程度']
	
	for num in range(10):
		for num2 in range(6):
			qualityContent[qualityContent.index('@' + str(num) + '-' + str(num2))] = question[num+1][num2]
			
		makePieChart('html/@' + str(num) + '-6.png' , question[num+1], qualityPieTitle[num])
		print ("make chart " + str(num))
		
	qualityContent[qualityContent.index('@10-1')] = totalCopies
	qualityContent[qualityContent.index('@10-2')] = classData[0].encode('utf8')
	qualityContent[qualityContent.index('@10-3')] = datetime.now().year-1911
	qualityContent[qualityContent.index('@10-4')] = classData[1].encode('utf8')
	qualityContent[qualityContent.index('@10-5')] = classData[1].encode('utf8')
	

	writeDataToHtml("./html/qualityTemp.html",qualityContent)
	#os.remove("./html/qualityTemp.html")
	