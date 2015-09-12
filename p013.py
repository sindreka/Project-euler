f = open("p013.txt","r")

text = f.read()
sum = 0
for i in range(100):
    sum += int(text[(0+51*i):(13+51*i)])
print(str(sum)[0:10])