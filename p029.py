num = 100


li = []
su = 0
for a in range(2,num+1):
#	print("a: ", a)
	for b in range(2,num+1):
		if a**b not in li:
			li.append(a**b)
			su += 1

print(su)
