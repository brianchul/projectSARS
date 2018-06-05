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