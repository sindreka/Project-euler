num = 500
li1 = [i for i in range(2,num)]
lenli1 = len(li1)
li2 = [1 for i in range(lenli1)]
sum = 1

for i in range(lenli1):
	if li2[i] != 0:
		sum *= li1[i]
		n = 2
		while n*(i+2)-2 < lenli1:
			li2[n*(i+2)-2] = 0
			n += 1
print(sum)
