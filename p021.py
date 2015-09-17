def sumOfDevisors(num):
    sum = 0
    for i in range(1,num):
        if not num % i:
            sum += i
    return sum

totSum = 0
for i in range(1,10000):
    su = sumOfDevisors(i)
    if i == sumOfDevisors(su) and i != su:
        totSum += i

print(totSum)