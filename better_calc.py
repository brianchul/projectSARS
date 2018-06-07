# -*- coding: utf-8 -*-
import os
import time
#import win32com.client
from datetime import datetime
from pylab import figure, axes, pie, title, savefig
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
import numpy as np
import pdfkit


grade = [0 for n in range(4)]
q1 = [0 for n in range(6)]
q2 = [0 for n in range(6)]
q3 = [0 for n in range(6)]
q4 = [0 for n in range(6)]
q5 = [0 for n in range(6)]
q6 = [0 for n in range(6)]
q7 = [0 for n in range(6)]
q8 = [0 for n in range(6)]
q9 = [0 for n in range(6)]
q10 = [0 for n in range(6)]
question = [grade,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10]
rollBack = []
totalCopies = 0
adviseList = []
addAdviseHeader = ["<p><strong>","</strong><strong></strong></p>\n"]
docTitle = ""
classData = ["",""]


def rawInput():
	x = input(">>> : ")
	return str(x)

def rollBackData(oldData):
	oldData = oldData.split(' ')
	if oldData[len(oldData)-1] is "":
		oldData.remove("")
	oldData = map(int,oldData)
	for num2 in range(0,len(oldData)):
		question[num2][oldData[num2]-1] = question[num2][oldData[num2]-1]-1

def printData():
	print ("     1     2     3     4     5     6")
	print ("------------------------------------------------")

	for pNum in range(0,len(question)):
			l = len(question[pNum])
			print
			
			if pNum is 0:
				s = "GD   "
			else:
				s = "Q"+str(pNum) + "   "
			
			for pNum2 in range(0,l):
				s += str(question[pNum][pNum2]) + "     "
			print (s)

def clearScreen():
	os.system('cls' if os.name == 'nt' else 'clear')

def readFile(readHtmlFileName):
	with open(readHtmlFileName, 'r',encoding='utf-8-sig') as f:
		content = f.readlines()
	# you may also want to remove whitespace characters like `\n` at the end of each line
	content = [x.strip() for x in content]
	f.close()
	return content
	
def writeDataToHtml(writeHtmlFileName,data):
	thefile = open(writeHtmlFileName, 'w',encoding='utf-8-sig')
	for item in data:
		print>>thefile, item
	thefile.close()

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
	
def makeBarChart(chartData):	

	n_groups = 10

	means_men = chartData
	fig, ax = plt.subplots()

	index = np.arange(n_groups)
	bar_width = 0.35

	opacity = 0.4
	error_config = {'ecolor': '0.3'}

	rects1 = plt.bar(index, 
					means_men, 
					bar_width,
					alpha=opacity,
					color='b',
					label='result')
	plt.xlabel('Question')
	plt.ylabel('Scores')
	plt.title('')
	plt.xticks(index + bar_width / 2, (1,2,3,4,5,6,7,8,9,10))
	plt.legend()

	plt.tight_layout()
	savefig('html/quantifyPlot.png')
	plt.clf()

def makePieChart(fileName,chartData,chartTitle):
	#zhfont1 = FontProperties(fname='C:\Windows\Fonts\arial.ttf')
	x = ['1分', '2分', '3分', '4分', '5分', '6分']
	y = np.array(chartData)
	colors = ['black','red','gold','lightskyblue','darkgreen','violet']
	percent = 100.*y/y.sum()
	explode = (0.05, 0.05, 0.05, 0.05, 0.05, 0.05)
	plt.axis('equal')
	patches, texts = plt.pie(y, colors=colors,explode=explode, startangle=90, radius=1)

	labels = [('{0} - {1:1.2f} %').format(i,j) for i,j in zip(x, percent)]

	plt.legend(patches, labels, loc='best', bbox_to_anchor=(-0.05, 1.),fontsize=10)
	plt.savefig(fileName, bbox_inches='tight')
	plt.clf()
		
def inputData():
	global totalCopies,classData,className,docTitle
	print ("輸入社課日期:(ex:12月6號)")
	classData[0] = rawInput()
	print ("輸入講師名稱:")
	classData[1] = rawInput()
	docTitle =  classData[0] + classData[1] + '滿意度'


	while True:
		err = 0
		print ("使用說明:將滿意度上面的數字已連續並在數字間加入空白 EX:3 6 5 6 5 5 6 6 6 6 6")
		print ("輸入88來返回上一步")
		print ("輸入99來完成報表")
		print ("目前份數:" + str(totalCopies))
		print ()
		printData()
		print('\n')
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
				print ("你目前還沒輸入資料!")
				print()
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
				print ("輸入錯誤")
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
				print ("資料格式錯誤")
				err = 1
				continue
		if err != 1:
			rollBack.append(appendData)
			totalCopies = totalCopies + 1

		clearScreen()
	
def finishData():
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
	
def calculateQuantifyData():
	quantifyData = []
	for num in range(1,11):
		sum = 0
		for num2 in range(6):
			if question[num][num2] != 0:
				sum = sum + question[num][num2] * num2+1	#num2從1開始 不然統計不正確
		quantifyData.append(round(sum/totalCopies,1))
	return quantifyData

def generateDoc1(adviseList):
	global docTitle
	
	adviseContent = readFile("./html/advise.html")
	
	for num in range(len(adviseList)):
		adviseContent.append(adviseList[num])
	#或許可以用讀檔的方式避免錯誤roll back

	adviseContent[adviseContent.index('@total')] = totalCopies
	for num in range(4):
		adviseContent[adviseContent.index('@g' + str(num))] = grade[num]
	
	for num in range(6):
		for num2 in range(10):
			adviseContent[adviseContent.index('@' + str(num2) + '-' + str(num))] = question[num2+1][num] #without grade
			
	writeDataToHtml("./html/adviseTemp.html",adviseContent)
	#convertHtmlToDoc("./html/adviseTemp.html",docTitle)
	#os.remove("./html/adviseTemp.html")
	
def generateDoc2():
	quantifyContent = readFile("./html/quantify.html")
	quantifyAdvise = readFile("./html/quantifyAdvise.txt")
	quantifyData = calculateQuantifyData()
	print ("making bar chart...")
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
	quantifyContent[quantifyContent.index("@10-2")] = docTitle
	writeDataToHtml("./html/quantifyTemp.html",quantifyContent)
	#convertHtmlToDoc("./html/quantifyTemp.html", docTitle + "quantify")
	#os.remove("./html/quantifyTemp.html")

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
	#convertHtmlToDoc("./html/qualityTemp.html", docTitle + u'quality')
	#os.remove("./html/qualityTemp.html")
	
inputData()
finishData()
print ("generating Doc1...")
generateDoc1(adviseList)
print ("generating Doc2...")
generateDoc2()
print ("generating Doc3...")
generateDoc3()
print ("complete")