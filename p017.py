count = 0
for i in range(1,1000):
    print(i)
    if i >= 100:
        count += 7
        if str(i)[0] == "1" or str(i)[0] == "2" or str(i)[0] == "6":
            count += 3
            print("100, 200 or 600")
        elif str(i)[0] == "3" or str(i)[0] == "7" or str(i)[0] == "8":
            count += 5
            print("300, 700 or 800")
        elif str(i)[0] == "4" or str(i)[0] == "5" or str(i)[0] == "9":
            count += 4
            print("400, 500 or 900")
        if i % 100:
            print("and")
            count += 3
    if i % 100 >= 20:
        if str(i % 100)[0] == "2" or str(i % 100)[0] == "3" or str(i % 100)[0] == "8" or str(i % 100)[0] == "9":
            count += 6
            print("20, 30, 80 or 90")
        elif str(i % 100)[0] == "7":
            count += 7
            print("70")
        elif str(i % 100)[0] == "5" or str(i % 100)[0] == "6" or str(i % 100)[0] == "4":
            count += 5
            print("50, 60 or 40")
    if 10 <= i % 100 < 20:
        if i % 100 == 10:
            count += 3
            print("10")
        elif i % 100 == 11 or i % 100 == 12:
            count += 6
            print("11 or 12")
        elif i % 100 == 13 or i % 100 == 14 or i % 100 == 19 or i % 100 == 18:
            count += 8
            print("13, 14,18 or 19")
        elif i % 100 == 15 or i % 100 == 16:
            count += 7
            print("15 or 16")
        elif i % 100 == 17:
            count += 9
            print("17")
    if (0 < i % 100 < 10) or (100 > i % 100 >= 20):
        if i % 10 == 1 or i % 10 == 2 or i % 10 == 6:
            count += 3
            print("1, 2 or 6")
        elif i % 10 == 3 or i % 10 == 7 or i % 10 == 8:
            count += 5
            print("3, 7 or 8")
        elif i % 10 == 4 or i % 10 == 5 or i % 10 == 9:
            count += 4
            print("4, 5 or 9")
print(count)
print(count+11)
