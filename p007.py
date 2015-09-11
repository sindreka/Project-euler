def isPrime(num,li):
	for element in li:
		if not num%element or element**(0.5)>num:
			return
	li.append(num)

def main(num):
	li = []
	li.append(2)
	candidate = 3
	while len(li) < num:
		isPrime(candidate,li)
		candidate += 2
	return li[-1]
print(main(10001))
