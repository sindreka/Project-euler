f1 = 1
f2 = 1
n = 2

while f2 < 10**999:
    f2,f1 = f2+f1,f2
    n += 1
print(n)
