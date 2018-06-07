# -*- coding: utf-8 -*-
import os
import time

import pdfkit
from datetime import datetime
from pylab import figure, axes, pie, title, savefig
import matplotlib.pyplot as plt
import numpy as np


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
addAdviseHeader = ["<p><strong>","</strong></p>\n"]
docTitle = ""
classData = ["", "", ""] #date, teacherName, classroom
hasQualityAdvise = False
qualityAdvise = ""


def rawInput():
	x = input(">>> : ")
	return str(x)

def rollBackData(oldData):
	oldData = oldData.split(' ')
	if oldData[len(oldData)-1] is "":
		oldData.remove("")
	oldData = list(map(int,oldData))
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
	
def writeDataToHtml(writeHtmlFileName, data):
	thefile = open(writeHtmlFileName, 'w',encoding='utf-8-sig')
	for item in data:
		thefile.write(item + '\n')
		#print (thefile, item)
	thefile.close()

'''
def convertHtmlToDoc(htmlName, docName):
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
'''

def convertHtmlToPDF(htmlPath, pdfName):
	pdfkit.from_file(htmlPath, outputPath(pdfName + '.pdf'))

def htmlPath(htmlName):
	return './html/' + htmlName

def outputPath(fileName):
	return './finished/' + fileName

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
	savefig(htmlPath("quantifyPlot.png"))
	plt.clf()

def makePieChart(fileName,chartData):
	x = ['1', '2', '3', '4', '5', '6']
	y = np.array(chartData)
	colors = ['black','red','gold','lightskyblue','darkgreen','violet']
	percent = 100.*y/y.sum()
	explode = (0.05, 0.05, 0.05, 0.05, 0.05, 0.05)
	plt.axis('equal')
	patches = plt.pie(y, colors=colors,explode=explode, startangle=90, radius=1)

	labels = [('{0} - {1:1.2f} %').format(i,j) for i,j in zip(x, percent)]

	plt.legend(patches, labels, loc='best', bbox_to_anchor=(-0.05, 1.),fontsize=10)
	plt.savefig(fileName, bbox_inches='tight')
	plt.clf()
		
def inputData():
	global totalCopies,classData,docTitle
	print ("輸入社課日期:(ex:12月6號)")
	classData[0] = rawInput()
	print ("輸入講師名稱:")
	classData[1] = rawInput()
	docTitle =  classData[0] + classData[1] + '滿意度'
	print("輸入社課教室:")
	classData[2] = rawInput()


	while True:
		err = 0
		print ("使用說明:將滿意度上面的數字已連續並在數字間加入空白 EX:3 6 5 6 5 5 6 6 6 6 6")
		print ("輸入88來返回上一步")
		print ("輸入99來完成報表")
		print ("目前份數:" + str(totalCopies))

		printData()
		print()
		print("     ↓↓↓↓↓↓↓↓↓↓↓")
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
				data = list(map(int,data))
				print(data)
				print

			except:
				print ("輸入錯誤")
				print("\n")
				err = 1
				clearScreen()
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
				clearScreen()
				continue

		if err != 1:
			rollBack.append(appendData)
			totalCopies = totalCopies + 1

		clearScreen()
	
def finishData():
	global adviseList, qualityAdvise, hasQualityAdvise
	countAdvise = 0
	
	# using while will cause extra loop
	while True:
		clearScreen()
		print ("已輸入內容: ")
		for num in range(len(adviseList)):
			print (adviseList[num])
		print ("輸入88來復原")
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

	print("是否要輸入質化心得?(Y/N或其他值)")
	ask = rawInput()
	if ask is "Y" or ask is "y":
		hasQualityAdvise = True
		print("輸入心得:")
		qualityAdvise = str(rawInput())
	elif ask is "N" or ask is "n":
		pass
	clearScreen()

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
	
	adviseContent = readFile(htmlPath("advise.html"))
	
	for num in range(len(adviseList)):
		adviseContent.append(adviseList[num])
	#或許可以用讀檔的方式避免錯誤roll back

	modifyKeyword('@total', adviseContent, totalCopies)
	#adviseContent[adviseContent.index('@total')] = totalCopies
	for num in range(4):
		modifyKeyword('@g'+ str(num), adviseContent, grade[num])
		#adviseContent[adviseContent.index('@g' + str(num))] = grade[num]
	
	for num in range(6):
		for num2 in range(10):
			modifyKeyword('@' + str(num2) + '-' + str(num), adviseContent, question[num2+1][num])
			#adviseContent[adviseContent.index('@' + str(num2) + '-' + str(num))] = question[num2+1][num] #without grade
			
	writeDataToHtml(htmlPath("adviseTemp.html"),adviseContent)
	convertHtmlToPDF(htmlPath("adviseTemp.html"), docTitle)
	os.remove(htmlPath("adviseTemp.html"))
	
def generateDoc2():
	quantifyContent = readFile(htmlPath("quantify.html"))
	quantifyAdvise = readFile(htmlPath("quantifyAdvise.txt"))
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

		modifyKeyword("@info", quantifyContent, docTitle)

		modifyKeyword("@" + str(num) + "-0", quantifyContent, quantifyData[num])
		modifyKeyword("@" + str(num) + "-1", quantifyContent, "{:.2f}".format(round(quantifyData[num]/10,2)))
		modifyKeyword("@" + str(num) + "-2", quantifyContent, quantifyAdviseTemp)
		
		quantifyTotalScore += str(round(quantifyData[num]/10,2)) + "+"
		quantifyTotalScoreSum += round(quantifyData[num]/10,2)

	modifyKeyword("@10-0", quantifyContent, str(quantifyTotalScore[:-1]) + " = " + "{:.2f}".format(quantifyTotalScoreSum))
	modifyKeyword("@10-1", quantifyContent, "{:.2f}".format(quantifyTotalScoreSum) + " /6=" + str("{:.2f}".format(round(quantifyTotalScoreSum/6,2)*100)) + "%")
	modifyKeyword("@10-2", quantifyContent, docTitle)

	writeDataToHtml(htmlPath("quantifyTemp.html"),quantifyContent)
	convertHtmlToPDF(htmlPath("quantifyTemp.html"), docTitle + "量化")
	os.remove(htmlPath("quantifyTemp.html"))

def generateDoc3():
	qualityContent = readFile(htmlPath("quality.html"))
	defaultAdvise = readFile(htmlPath("defaultQualityAdvise.txt"))[0]
	#qualityPieTitle = ['1.整體評價','2. 事前宣傳','3. 場地','4. 講師上課流暢度','5. 講師的上課速度','6.講師表達清晰度','7. 主題和內容的契合度','8. 內容理解程度','9.主題和內容契合度','10.內容吸引程度']
	
	for num in range(10):
		for num2 in range(6):
			modifyKeyword('@' + str(num) + '-' + str(num2), qualityContent, question[num+1][num2])
			
		makePieChart(htmlPath('@' + str(num) + '-6.png'), question[num+1])
		print ("make chart " + str(num))
	
	if hasQualityAdvise:
		modifyKeyword("@10-0", qualityContent, qualityAdvise)
	else:
		modifyKeyword("@10-0", qualityContent, defaultAdvise)
	modifyKeyword("@10-1", qualityContent, totalCopies)
	modifyKeyword("@10-2", qualityContent, classData[0])
	modifyKeyword("@10-3", qualityContent, datetime.now().year-1911)
	modifyKeyword("@10-4", qualityContent, classData[1])
	modifyKeyword("@10-5", qualityContent, classData[1])
	modifyKeyword("@classroom", qualityContent, classData[2])

	

	writeDataToHtml(htmlPath("qualityTemp.html"),qualityContent)
	convertHtmlToPDF(htmlPath("qualityTemp.html"), docTitle + "質化")
	os.remove(htmlPath("qualityTemp.html"))

def modifyKeyword(keyword,lists,modify):
    for content in lists:
        if keyword in content:
            pos = lists.index(content)
            lists[pos] = content.replace(keyword, str(modify))
    return lists

def main():
	global ask
	inputData()
	finishData()
	print ("generating Doc1...")
	generateDoc1(adviseList)
	print ("generating Doc2...")
	generateDoc2()
	print ("generating Doc3...")
	generateDoc3()
	print ("complete")
	time.sleep(5)
	print("是否填寫新的滿意度?(y/n)")
	ask = rawInput()

main()
if ask is 'y':
	main()
	clearScreen()
else:
	print("app by brianchul @ tkucsie 20180607")
	print("BYE")
	time.sleep(5)