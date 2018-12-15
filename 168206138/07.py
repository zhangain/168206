start = 'hit'
end = 'cog'
adict = ['hot', 'dot', 'dog', 'loc', 'hi', 'doge', 'lot', 'log']
count = []
count.append(start)
def xiang(adict, start):#在 adict 中找与 a 相似差异为 1 个单位的
	zhi = {}
	c = []
	for n in range(len(adict)):
		zhi[adict[n]] = 0
	for n in range(len(start)):
		for m in range(len(adict)):
			if len(adict[m]) == len(start):#单词长度一样 才有机会相似度 +1
				if start[n] == adict[m][n]:
					zhi[adict[m]] += 1
	for key,value in zhi.items():
		if value == len(start) - 1:
			c.append(key)
	return c

def zao(adict, start, end, en):	
	st = xiang(adict, start)
	for n in range(len(st)):
		if st[n] in count:
			continue
		count.append(st[n])
		start = st[n]
		if start in en:
			count.append(end)
			print(count)
			count.remove(end)
			count.remove(st[n])
		else:
			zao(adict, start, end, en)
			count.remove(st[n])
				

en = xiang(adict, end)
zao1 = zao(adict, start, end, en)
print(zao1)

