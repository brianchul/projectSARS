def inputData():
	global totalCopies,classData,className,docTitle
	print unicode("輸入社課日期:(ex:12月6號)",'utf-8')
	classData[0] = rawInput().decode('big5')
	print unicode("輸入講師名稱:",'utf-8')
	classData[1] = rawInput().decode('big5')
	docTitle =  classData[0] + classData[1] + u'滿意度'


	while True:
		err = 0
		print unicode("使用說明:將滿意度上面的數字已連續並在數字間加入空白 EX:3 6 5 6 5 5 6 6 6 6 6",'utf-8')
		print unicode("輸入88來返回上一步",'utf-8')
		print unicode("輸入99來完成報表",'utf-8')
		print unicode("目前份數:" + str(totalCopies),'utf-8')
		print
		printData()
		print
		print
		data = rawInput()
		appendData = data

		if data == "88":
			if totalCopies != 0:
				rollBackData(rollBack[totalCopies-1])
				rollBack.remove(rollBack[totalCopies-1])
				totalCopies = totalCopies - 1
				clearScreen()
				continue
			else:
				print unicode("你目前還沒輸入資料!",'utf-8')
				print
				time.sleep(3)
				clearScreen()
				continue
		elif data == "99":
			break
		else:
			"""	   
		if data == "show":
			print rollBack
			continue
			"""    
		if data != "99" and data != "88":

			try:
				data = data.split(' ')
				if data[len(data)-1] is "":
					data.remove("")
				data = map(int,data)
				print

			except:
				print unicode("輸入錯誤",'utf-8')
				print
				print
				err = 1
				continue
			check = 0
			try:
				for num2 in range(0,len(data)):
					question[num2][data[num2]-1] = question[num2][data[num2]-1]+1
					check = check + 1
			except:
				for num2 in range(0,check):
					question[num2][data[num2]-1] = question[num2][data[num2]-1]-1
				print unicode("資料格式錯誤",'utf-8')
				err = 1
				continue
		if err != 1:
			rollBack.append(appendData)
			totalCopies = totalCopies + 1

		clearScreen()