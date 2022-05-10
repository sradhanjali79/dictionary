x="MISSISSIPPI"
dic={}
for key in x:
    value=0
    for key1 in x:
        if key==key1:
            value+=1
    # if key not in dic:
    dic[key]=value
print(dic)