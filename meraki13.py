my_dict = {'a':50,'b':58,'c':56,'d':40,'e':100,'f':20}
max1=0
max2=0
max3=0
b=[]
for i in my_dict:
    if my_dict[i]>max1:
        max3=max2
        max2=max1
        max1=my_dict[i]
    elif my_dict[i]>max2:
        max2=my_dict[i]
    elif my_dict[i]>max3:
        max3=my_dict[i]
for i in my_dict:
    if max1==my_dict[i]:
        b.append(i)
    if max2==my_dict[i]:
        b.append(i)
    if max3==my_dict[i]:
        b.append(i)
print(b)

