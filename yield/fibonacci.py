def fibonacci(num):
	a,b = 0,1
	for i in range(num):
		temp = a
		a = b
		b = temp + b
		yield a

for val in fibonacci(10):
	print(val)