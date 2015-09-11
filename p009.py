num = 1000

for i in range(1,num-1):
	for j in range(1,num-i-1):
		k = num-i-j
		if i**2+j**2 == k**2:
			print("Sum: ",i+j+k)
			print("Product: ",i*j*k)
			quit()

