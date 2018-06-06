def makePieChart(fileName,chartData,chartTitle):

	x = ['1分', '2分', '3分', '4分', '5分', '6分']
	y = np.array(chartData)
	colors = ['black','red','gold','lightskyblue','darkgreen','violet']
	percent = 100.*y/y.sum()
	explode = (0.05, 0.05, 0.05, 0.05, 0.05, 0.05)
	plt.axis('equal')
	patches = plt.pie(y, colors=colors,explode=explode, startangle=90, radius=1)

	labels = [('{0} - {1:1.2f} %').format(i,j) for i,j in zip(x, percent)]

	plt.legend(patches, labels, loc='best', bbox_to_anchor=(-0.05, 1.),fontsize=10)
	plt.title(chartTitle)
	plt.savefig(fileName, bbox_inches='tight')
	plt.clf()
