start = 'hit'
end = 'cog'
count = []
count.append(start)
def huang(start, end):
	for s in range(0, int(len(start))):
		for z in range(ord('a'), ord('z')+1):
			start[s] = chr(z)
			if start[s] == end[s]:
				c = ''
				for s in range(0, int(len(start))):
					c += start[s]
				count.append(c)
				break

astart = []
for s in range(0, int(len(start))):
	astart.append(start[s])	
huang(astart, end)
print("路径：")
print(count)
