from die import Die
import pygal

die1 = Die()
die2 = Die()
results = []

for roll_num in range(100):
	result1 = die1.roll()
	result2 = die2.roll()
	results.append(result1+result2)



#分析结果
frequencies = []
for value in range(1,2*die1.num_sides+1):
	frequency = results.count(value)
	frequencies.append(frequency)

hist = pygal.Bar()

hist.add('D6',frequencies)
hist.render_to_file('die_visual.svg')