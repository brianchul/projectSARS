def inputData():
	global totalCopies,classData,className,docTitle
	print ("輸入社課日期:(ex:12月6號)")
	classData[0] = rawInput()
	print ("輸入講師名稱:")
	classData[1] = rawInput()
	docTitle =  classData[0] + classData[1] + '滿意度'