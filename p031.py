def listMult(li1,li2):
	su = 0
	for i in range(len(li1)):
		su += li1[i]*li2[i]
	return su
def numComb(coins,su):
	li = [0 for i in range(len(coins))]
	count = 0
	current = len(coins) - 1
	n = 0
	while li[0] < su:
		for i in reversed(range(current + 1)):
			while su >= listMult(coins,li) + coins[i]:
				li[i] += 1
		count += 1
		current = 0
		while li[current+1] == 0 and current < 6 :
			current += 1
		if li[current +1] > 0:
			li[current+1] -= 1
		else:
			break
		li[0] = 0
	return count

coins = [1,2,5,10,20,50,100,200]
su = 200


print(numComb(coins,su))

