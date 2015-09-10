import math
import copy

def divby(number):
    k = 0
    li = []
    for i in reversed(range(round(math.sqrt(number)))):
        if i > 1 and (number/i == round(number/i)):
            k = 1
            li.append(i)
    if k == 0:
        li.append(number)
    return li

def main():
    number = float(600851475143)
    li1 = [number]
    li2 = []
    li3 = []
    while li1 != li3:
        li3 = copy.copy(li1)
        for element in li1:
            temp_li = divby(element)
            for elem in temp_li:
                li2.append(elem)
        li1 = copy.copy(li2)
        li2 = []
    print(sorted(li3)[-1])
main()