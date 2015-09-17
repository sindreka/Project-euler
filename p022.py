def quickSort(li):
    if len(li) > 1:
        pivot = li[0]
    else:
        return li
    li1 = []
    li2 = []
    for element in li[1:]:
        if element < pivot:
            li1.append(element)
        else:
            li2.append(element)
    return quickSort(li1) + [pivot] + quickSort(li2)



def openFile(filename):
    f = open(filename, 'r')
    text = f.read()
    names = []
    name = ""
    for letter in text:
        if letter == ",":
            names.append(name)
            name = ""
        elif "A" <= letter <= "Z":
            name += letter
    names.append(name)
    return names

def main(filename):
    names = openFile(filename)
    names = quickSort(names)
    totSum = 0
    for i in range(len(names)):
        thisName = list(names[i])
        nameSum = 0
        for letters in thisName:
            nameSum += ord(letters)-64
        totSum += nameSum*(i+1)
    return totSum
print(main("p022.txt"))