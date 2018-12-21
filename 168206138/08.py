"""
A：我没有偷钻石。
B：D就是罪犯。
C：B是盗窃这块钻石的罪犯。
D：B有意诬陷我。
假定只有一个人说的是真话，编程序判断谁偷走了钻石。
"""
St = ['A','B','C','D']

print("小偷是：",end="")
for s in St:
	i = s  
	A=(i != 'A')
	B=(i == 'D')
	C=(i == 'B')
	D=(i != 'D')
	if (A + B + C + D == 1):
		lists = [A,B,C,D]
		print(i,end=" ")
		print("\n说真话的是：",end="")
		for i in range(len(lists)):
			if lists[i]:
				print(St[i],end=" ")
