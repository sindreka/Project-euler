def isPrime(num):
	for i in range(2,round(num**0.5+0.6)):
		if num % i == 0:
			return 0
	return 1

num = 20
li = []
for i in range(2,num):
	if isPrime(i):
		li.append(i)

minProd = 1
for element in li:
	exponent = 1
	while element**exponent <= num:
		minProd *= element
		exponent += 1
print(minProd)
