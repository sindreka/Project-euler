def pandigital(strin,n):
	if len(strin) == n:
		for i in range(len(strin)-1):
			if strin[i] == '0' or  strin[i] in strin[:i] or strin[i] in strin[1+i:]:
				return 0

	return 1

def multiplenumbers(num):
	if '0' in num:
		return 0
	for i in range(len(strin)-1)
		if strin[i] == '0' or  strin[i] in strin[:i] or strin[i] in strin[1+i:]:
			return 0
	return 1

def sivert(n):
	li = []
	for i in range(1,n):
		j = 1
		while i*j < n:
				

su = 0



for i in range(2,987654321):
	tempStr = ''
	tempprod = 1
	for j in range(2,round(i**0.5+0.6)):
		if not i % j :
			tempStr += str(j)
			tempprod *= j
	if pandigital(tempStr,9):
		su += tempprod
	print(i)
