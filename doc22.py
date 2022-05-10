# x={"1":['a','b'], "2":['c','d']}
# for i in x["1"]:
#     for j in x["2"]:
#         print(i+j)


x={"1":['a','b'], "2":['c','d']}
a,b=x.values()
for i in a:
    for j in b:
        print(i+j)




