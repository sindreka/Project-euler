counter = 0
number = 500
current = 3
next = 3

import math

#while current < pow(2,20):
#    current += next
#    next += 1



while counter <= 500:
    counter = 2
    current += next
    next += 1
    for i in range(2,round(math.sqrt(current)+0.6),1):
        if not current%i:
            counter += 2
print(current)

