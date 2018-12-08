start = 'hit'
end = 'cog'
adict = ['hot','dot','dog','lot','log']
count = []
count.append(start)
def xiang(adict, a):
	zhi = {}
	c = []
	for n in range(len(adict)):
		zhi[adict[n]] = 0
	for n in range(len(a)):
		for m in range(len(adict)):
			if a[n] == adict[m][n]:
				zhi[adict[m]] += 1
	for key,value in zhi.items():
		if value == 2:
			c.append(key)
	return c

def zao(adict, start, end, en):	
	st = xiang(adict, start)
	if len(st) == 0:
		return 
	for n in range(len(st)):
		if st[n] in count:
			continue
		count.append(st[n])
		start = st[n]
		if start in en:
			count.append(end)
			print(count)
			count.remove(end)
		else:
			zao(adict, start, end, en)
				

en = xiang(adict, end)
zao1 = zao(adict, start, end, en)
print(zao1)
