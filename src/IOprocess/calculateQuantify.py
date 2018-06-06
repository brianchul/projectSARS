def calculateQuantifyData():
	quantifyData = []
	for num in range(1,11):
		sum = 0
		for num2 in range(6):
			if question[num][num2] != 0:
				sum = sum + question[num][num2] * num2+1	#num2從1開始 不然統計不正確
		quantifyData.append(round(sum/totalCopies,1))
	return quantifyData