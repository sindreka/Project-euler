sum = 0
fib1 = 1
fib2 = 1
while fib2 <= 4000000:
    fib2,fib1 = fib1+fib2,fib2
    if not fib2%2:
        sum +=fib2
print(sum)