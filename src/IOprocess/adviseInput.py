def adviseInput():
	global adviseList
	countAdvise = 0
	
	# using while will cause extra loop
	while True:

		print ("TotalInput: ")
		for num in range(len(adviseList)):
			print (adviseList[num])
		print ("輸入88來回到上一步(""注意動作無法復原,絕對不是我懶得寫code :D"")")
		print ("輸入99來完成")
		print ("輸入心得及建議:")
		inputAdvise = rawInput()

		if inputAdvise == "99":
			break
		elif inputAdvise == "88":
			adviseList = adviseList[:-1]
			continue
		else:
			print ("inputAdvise2:" + inputAdvise)
			
		clearScreen()
		countAdvise = countAdvise + 1
		adviseList.append(addAdviseHeader[0] + str(countAdvise) + ". " + inputAdvise + addAdviseHeader[1])
