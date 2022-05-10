x=int(input("enter..."))
dic={}
for i in range(1,x+1):
    z=[]
    for j in range(1,11):
        z.append(i*j)
    dic[i]=z
print(dic)
