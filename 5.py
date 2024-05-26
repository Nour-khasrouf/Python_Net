b = list(input("Input a binary number: "))
x = 0

for i in range(len(b)):
	d = b.pop()
	if d == '1':
		x = x + pow(2, i)
print("The decimal ", x)


