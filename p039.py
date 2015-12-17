
import math

def integerTriangle(a,b):
	if not (pow(a,2)+pow(b,2))**0.5 % 1:
		return 1
	return 0
def main():
	ma = 0
	num = -1
	for num in range(120,1000):
		temp = 0
		for a in range(1,num-2):
			b = 1
			while a+b< num-1:
				temp += integerTriangle(a,b)
				b += 1
		if temp > ma:	
			ma = temp
			maxint = num			
	return maxint
print(main())
