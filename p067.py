def getText(filename):
	f = open(filename,"r")
	text = f.read()
	num = ""
	li = []
	mat = []
	for i in range(len(text)):
		if text[i] == "\n":
			mat.append(li)
			li = []
		elif text[i] == " ":
			li.append(int(num))
			num = ""
		else:
			num += text[i]
			if i+1 < len(text) and text[i+1] == "\n":
				li.append(int(num))
				num = ""
	li.append(int(num))
	mat.append(li)
	return mat

def smartAlgorithm(mat):
	copyOfList = mat[:][:]
	for i in reversed(range(1,len(copyOfList[-1]))):
		for j in range(len(copyOfList[i])-1):
			copyOfList[i-1][j] += max(copyOfList[i][j],copyOfList[i][j+1])
	return copyOfList[0][0]

print(smartAlgorithm(getText("p067.txt")))

