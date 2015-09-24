def powerOfFive(i):
	li = str(i)
	su = 0
	for letter in li:
		su += int(letter)**5
	return su

su = 0
for i in range(2,6*9**5):
	if powerOfFive(i) == i:
		su += i

print(su)
