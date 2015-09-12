def getFile(filename):
	f = open(filename,'r')
	text = f.read()
	mat = [[int(text[60*i+j*3]+text[j*3+1+60*i]) for j in range(20)] for i in range(20)]
	return mat

def right(mat,i,j):
	return mat[i][j]*mat[i+1][j]*mat[i+2][j]*mat[i+3][j]
def down(mat,i,j):
	return mat[i][j]*mat[i][j+1]*mat[i][j+2]*mat[i][j+3]
def diagonal(mat,i,j):
	return mat[i][j]*mat[i+1][j+1]*mat[i+2][j+2]*mat[i+3][j+3]
def otherdiagonal(mat,i,j): 
	return mat[i][j]*mat[i-1][j+1]*mat[i-2][j+2]*mat[i-3][j+3]

def main(filename):
	prod = 0
	mat = getFile(filename)
	for i in range(0,20-4,1):
		for j in range(0,20-4,1):
			prod = max(prod,diagonal(mat,i,j))
	
	for i in range(0,20-4,1):
		for j in range(0,20,1):
			prod = max(prod,right(mat,i,j))
	
	for j in range(0,20,1):
		for j in range(0,20-4,1):
			prod = max(prod,down(mat,i,j))

	for i in range(3,20,1):
		for j in range(0,20-4,1):
			prod = max(prod,otherdiagonal(mat,i,j))	
	return prod
print(main("p011.txt"))
