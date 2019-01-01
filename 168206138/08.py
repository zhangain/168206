"""
A：我没有偷钻石。
B：D就是罪犯。
C：B是盗窃这块钻石的罪犯。
D：B有意诬陷我。
假定只有一个人说的是真话，编程序判断谁偷走了钻石。
"""
thief = ['A','B','C','D']

for s in thief:
	i = s  
	A=(i != 'A')
	B=(i == 'D')
	C=(i == 'B')
	D=(i != 'D')
	if (A + B + C + D == 1):	
		lists = [A,B,C,D]
		print("\n如果说真话的是：",end="")
		for p in range(len(lists)):
			if lists[p]:
				print(thief[p],end=" ")
		print("\n")
		print("小偷是：",end="")
		print(i)
#参考文献https://www.cnblogs.com/zdz8207/archive/2012/12/17/2821708.html
