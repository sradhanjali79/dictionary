dic={"ball":"red","bat":4,"wickets":8,"ball":"green","bat":3}
x={}
for key,value in dic.items():
    if value not in x.values():
        x[key]=value
print(x)





