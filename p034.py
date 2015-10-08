import math
import time
su = 0

i = 3
while i < 2550000:
	tempSum = 0
	for value in str(i):
		tempSum += math.factorial(int(value))
	if math.ceil(i/10.0)*10 < tempSum:
		i = math.ceil(i/9.9999999999999)*10-1
	if i == tempSum:
		su += i
	i += 1
print(su)
