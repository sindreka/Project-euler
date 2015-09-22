def spiralMatrix(num):
    mat = [[0 for i in range(num)] for j in range(num)]
    counter = 2
    centre = int((num-1)/2)
    i = centre
    j = centre
    current = 2
    mat[centre][centre] = 1
    mat[centre][centre+1] = 2
    while current < num**2:
        j += 1
        mat[i][j] = current
        current += 1
        for k in (range(1,counter*2-2)):
            i += 1
            mat[i][j] = current
            current += 1
        for k in (range(1,counter*2-1)):
            j -= 1
            mat[i][j] = current
            current += 1
        for k in range(1,counter*2-1):
            i -= 1
            mat[i][j] = current
            current += 1
        for k in range(1,counter*2-1):
            j += 1
            mat[i][j] = current
            current += 1
        counter += 1

    j += 1
    mat[0][-1] = num**2
    current += 1
    return mat
num = 1001
mat = spiralMatrix(num)

su = 0

for i in range(round((num-1)/2)):
    su += mat[i][i] + mat[i][num-1-i] + mat[num-1-i][i] + mat[num-1-i][num-1-i]
su += 1
print(su)