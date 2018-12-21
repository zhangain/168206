St = ['A','B','C','D']

print("小偷是：")
for s in St:
	i = s
	A=(i != 'A')
	B=(i == 'D')
	C=(i == 'B')
	D=(i != 'D')
	if (A + B + C + D == 1):
		print(i)
