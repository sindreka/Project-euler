num = 1000000
maxCount = 0
maxN = 0
for i in range(2,num):
    n = i
    counter = 0
    while n != 1:
        if n%2:
            n = 3*n+1
            counter += 1
        else:
            n /= 2
            counter += 1
    if counter > maxCount:
        maxCount = counter
        maxN = i


print(maxN)