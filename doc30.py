a={'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
dic={}
for key,value in a.items():
    x=""
    for j in key:
        if j!=" ":
            x=x+j
    dic[x]=value
print(dic)


