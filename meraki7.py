x=[{"first":"1"},{"second": "2"},{"third": "1"},{"four": "5"},{"five":"5"},{"six":"9"},{"seven":"7"}]
dic=[]
for i in x:
    for value in i:
        y=i[value]
        if y not in dic:
            dic.append(y)
print(dic)