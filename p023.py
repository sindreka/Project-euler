li = [0 for i in range(1,28123+1)]
for i in range(1,28123+1):
    n = 2
    while i*n < 28123:
        li[i*n] += i
        n += 1

abundantNumbers = []
for i in range(len(li)):
    if li[i] > i+1:
        abundantNumbers.append(i)
li = [i for i in range(1,28123+1)]

for number1 in abundantNumbers:
    for number2 in abundantNumbers:
        if number1+number2-1 < 28123:
            li[number1+number2-1] = 0
print(sum(li))
