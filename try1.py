a=input("enter...")
z=[]
dic={}
j=1
c=0
y=a.split()
for i in a:
    if i==" ":
        c=c+1
        z.append(c)
for i in y:
    dic["item"+str(j)]=i 
    for k in z:
        dic["space"+str(j)]=k
        z.remove(k)
        break    
    j=j+1
print(dic)