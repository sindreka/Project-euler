def isLeapYear(year):
    if year % 4 and not year % 400:
        return 0
    return 1
def daysInMonth(year):
    temp = [31,28,31,30,31,30,31,31,30,31,30,31]
    ans = []
    temp[2] += isLeapYear(year)
    for days in temp:
        i = 1
        for day in range(days):
            ans.append(i)
            i = 0
    return ans

daysOfWeek = [1,0,0,0,0,0,0]
year = 1901
months = []
weeks = []
for year in range(1901,2001):
    thisYear = daysInMonth(year)
    for day in thisYear:
        months.append(day)
while len(weeks) < 366*100:
    for day in daysOfWeek:
        weeks.append(day)
weeks.pop(0)
sum = 0
for i in range(len(months)):
    sum += weeks[i]*months[i]
print(sum)




