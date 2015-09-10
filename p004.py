def isPalindrome(num):
    temp = str(num)
    length = len(temp)
    for i in range(round(length/2)):
        if temp[i] != temp[length-i-1]:
            return 0
    return 1

def main():
    num = 1
    for i in reversed(range(100,999)):
        for j in reversed(range(100,999)):
            if isPalindrome(i*j) and num < i*j:
                num = i*j
                #return i*j
    return num

print(main())