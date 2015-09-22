def func(a,b,n):
    return n**2 + n*a + b
num = 1000
numbers = func(num,num,num)
primes = [1 for i in range(numbers)]
primes[0] = 0
primes[1] = 0
for i in range(2,numbers):
    n = 2
    while n*i < numbers:
        primes[n*i] = 0
        n += 1
maxRep = 0
maxProd = -1
for a in range(-num,num):
    for b in range(-num,num):
        n = 0
        while 1:
            if primes[func(a,b,n)]:
                n += 1
            else:
                break
        if maxRep < n:
            maxRep = n
            maxProd = a*b
print(maxProd)
