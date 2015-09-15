def getText(filename):
	f = open(filename,"r")
	text = f.read()
	num = ""
	li = []
	mat = []
	for i in range(len(text)):
		if text[i] == '\n':
			mat.append(li)
			li = []
		elif text[i] == " ":
			li.append(int(num))
			num = ""
		elif 1 <= int(text[i]) < 10:
			num += text[i]
			if text[i+1] == "\n":
				li.append(int(num))
				num = ""
				
	return mat
getText("p018.txt")

def nextPosition(mat,row,col,val,i):
	row += 1
	col += i
	print("row: ", row, "col: ", col)
	val += mat[row][col]
	return col,row,val

def searchAlgorithm(mat,row,col,val):
	newVal = [float('Inf'),float('Inf')]
	#val = 0
	dummy = 0
	while row < 15 and  dummy == 0:
		for i in [0,1]:
			row,col,val = nextPosition(mat,row,col,val,i)
			if row < 15:
				newVal[i] = searchAlgorithm(mat,row,col,val)
			else:
				dummy = 1
	return max(newVal[0],newVal[1])

print(searchAlgorithm(getText("p018.txt"),0,0,0))

