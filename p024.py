
def permutation(li):
    if li[-1] > li[-2]:
        return li[:-2] + [li[-1], li[-2]]
    else:
        for i in range(3, len(li)+1,1):
            for j in range(1,i+1):
                if li[-j] > li[-i]:
                    li[-i], li[-j] = li[-j], li[-i]
                    return li[:-i+1] + sorted(li[-i+1:])

        return li
num = 10
perm = 10**6
li = [i for i in range(num)]
for i in range(perm-1):
    li = permutation(li)
ans = ""
for element in li:
    ans += str(element)
print(ans)



