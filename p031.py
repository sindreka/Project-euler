def listMult(li1,li2):
	su = 0
	for i in range(len(li1)):
		su += li1[i]*li2[i]
	return su
def numComb(coins,su):
	li = [0 for i in range(len(coins))]
	count = 0
	current = len(coins)-1
	n = 0
	while li[0] < su and n < 10:
		n += 1
		for i in reversed(range(current+1)):
			while su >= listMult(coins,li) + coins[i]:
				li[i] += 1
		count += 1
		print("count: ", count ,"li: ", li)
		#count += 1
		if current > 0 and  li[current] > 0:
			li[current] -= 1
			current -= 1 
		elif current == 1:# or (len(li)-1 > current  and  li[current+1] == 0):
			li[current+1] = 0
			#current += 1
	#	else: 
#			current -= 1
		li[0] = 0
	return count

coins = [1,2,5,10,20,50,100,200]
su = 200

#numCoins = [0,0,0,0,0,0,0,0]

print(numComb(coins,su))


#print(listMult(coins,numCoins))



