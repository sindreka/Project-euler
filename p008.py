f = open("p008.txt","r")
text = f.read()
num = 13
maxprod = 1
for i in range(len(text)-num):
	prod = 1
	for j in range(num):
		prod *= int(text[i+j])
	if prod > maxprod:
		maxprod = prod
print(maxprod)
