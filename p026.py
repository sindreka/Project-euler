def getPeriod(siz,num):
	from decimal import getcontext
	from decimal import Decimal
	getcontext().prec = 10000
	li = (str(round(Decimal(siz)/Decimal(num))))
	li = li[:-5]
	le = len(li)
	period = 1
	for i in reversed(range(len(li))):
		if li[i-1] == li[-1]:
			for j in range(len(li[i:])):
				if li[i:][j] != li[2*i-le:i][j]:
					period += 1
					break
			else:
				return period
		else:
			period += 1

maxPeriod = 0
siz = 10**10000
period = -1
for i in range(3,1000):
	period = getPeriod(siz,i)
	if maxPeriod < period:
		maxPeriod = period
		maxNum = i
print(maxNum)
