# -*- coding: utf-8 -*-
import time



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

inputData()
finishData()
print ("generating Doc1...")
generateDoc1(adviseList)
print ("generating Doc2...")
generateDoc2()
print ("generating Doc3...")
generateDoc3()
print ("complete")