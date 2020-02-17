import json
import pygal
import math
from itertools import groupby


filename = 'btc_close_2017.json'
with open(filename) as f:
	btc_data = json.load(f)
dates,months,weeks,weekdays,closes = [],[],[],[],[]

for btc_dict in btc_data:
	date = btc_dict['date']
	month = btc_dict['month']
	week = btc_dict['week']
	weekday = btc_dict['weekday']
	close = int(float(btc_dict['close']))
	dates.append(date)
	months.append(month)
	weeks.append(week)
	weekdays.append(weekday)
	closes.append(close)
print(dates,months,weeks,weekdays,closes)


line_chart = pygal.Line(x_label_rotation=20,show_minor_x_labels=False)
line_chart.title = '收盘价()'
line_chart.x_labels = dates
N = 20
line_chart.x_labels_major = dates[::N]
#close_log = [math.log10(_) for _ in closes]#用对数表示
line_chart.add('收盘价',closes)
line_chart.render_to_file('收盘图.svg')



def draw_linex(x_data,y_data,title,y_legend):
	xy_map = []
	for x,y in groupby(sorted(zip(x_data,y_data)),key=lambda _: _[0]):
		y_list = [v for _, v in y]
		xy_map.append([x,sum(y_list)/len(y_list)])
	x_unique, y_mean = [*zip(*xy_map)]
	line_chart = pygal.Line()
	line_chart.title = title
	line_chart.x_labels = x_unique
	line_chart.add(y_legend,y_mean)
	line_chart.render_to_file(title+'.svg')
	return line_chart

idx_month = dates.index('2017-12-01')
line_chart_month = draw_linex(months[:idx_month], closes[:idx_month],'values of everyday in every month ','riyuejunjia')





