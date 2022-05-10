x={"bably":3,"shraddha":6,"dipti":2,"biki":8}
dic={}
z=[]
b=[]
for i,j in x.items():
	z.append(j)
	b.append(i)
z.sort()
for p in b:
	for q in z:
		dic[p]=q
		z.remove(q)
		break
print(dic)