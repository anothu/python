import csv
from datetime import datetime
import matplotlib.pyplot as plt


filename = 'death_valley_2014.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	dates, highs = [], []

	for row in reader:
		current_date = datetime.strptime(row[0],"%Y-%m-%d")
		high = int(row[1])
		dates.append(current_date)
		highs.append(high)

	print(highs)
	fig =  plt.figure(dpi=64, figsize=(15, 6))
	plt.plot(dates,highs,c='red', alpha=0.5)
	
	#fig.autofmt_xdate()

	#设置x，y轴
	plt.show()
