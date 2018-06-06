def printData(question):
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