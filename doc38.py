x={'c1': 'Red', 'c2': 'Green', 'c3': None}
dic={}
for key,value in x.items():
    if value!=None:
        dic[key]=value
print(dic)