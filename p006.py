n = 100

sum1 = (n*(n+1)/2)**2

for i in range(n+1):
	sum1 -= i**2

print(sum1)
