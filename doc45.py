x=[{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]
n=input("enter...")
for i in x:
    for key,value in i.items():
        if key=="id" and value==n:
            x.remove(i)
print(x)

    