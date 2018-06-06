def rollBackData(oldData,lists):
	oldData = oldData.split(' ')
	if oldData[len(oldData)-1] is "":
		oldData.remove("")
	oldData = map(int,oldData)
	for num2 in range(0,len(oldData)):
		lists[num2][oldData[num2]-1] = lists[num2][oldData[num2]-1]-1