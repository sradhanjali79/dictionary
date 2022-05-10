dic={"a":[4,3,1],"b":[4,6],"c":[2,3]}
d={}
for i,j in dic.items():
    sum=0
    for p in j:
        sum+=p   
    dic[i]=sum
print(dic)
