num = 20
mat = [[1 for i in range(num+1)] for j in range(num+1)]
for i in range(1,num+1):
    for j in range(1,num+1):
        mat[i][j] = mat[i-1][j] + mat[i][j-1]
print(mat[num][num])