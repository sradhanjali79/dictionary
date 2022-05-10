x={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
dic={}
for i,j in x.items():
    z=[]
    for k in j:
        if k%2==0:
            z.append(k)
    dic[i]=z
print(dic)