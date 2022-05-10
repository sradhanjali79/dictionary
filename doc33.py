# x={'Aex':{'class':'V','rolld_id':2},'Puja':{'class':'V','roll_id':3}}
# for i in x:
#     print(i)
#     for j in x[i]:
#         print(j,":",x[i][j])

# def greet(*names):
#     for name in names:
#         print(name)
# greet("Monica", "Luke", "Steve", "John")

def greet(*names):
    i=0
    while i<len(names):
        if names[i] in names:

            print(names)
        i=i+1
greet("Monica", "Luke", "Steve", "John")

