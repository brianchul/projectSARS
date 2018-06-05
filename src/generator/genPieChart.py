def makePieChart(fileName,chartData,chartTitle):
	zhfont1 = FontProperties(fname='C:\Windows\Fonts\arial.ttf')
	x = [u'1分', u'2分', u'3分', u'4分', u'5分', u'6分']
	y = np.array(chartData)
	colors = ['black','red','gold','lightskyblue','darkgreen','violet']
	percent = 100.*y/y.sum()
	explode = (0.05, 0.05, 0.05, 0.05, 0.05, 0.05)
	plt.axis('equal')
	patches, texts = plt.pie(y, colors=colors,explode=explode, startangle=90, radius=1)

	labels = [unicode('{0} - {1:1.2f} %').format(i,j) for i,j in zip(x, percent)]

	plt.legend(patches, labels, loc='best', bbox_to_anchor=(-0.05, 1.),fontsize=10)
	plt.title(chartTitle)
	plt.savefig(fileName, bbox_inches='tight')
	plt.clf()
