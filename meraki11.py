# my_dict = {'a':50,'b':58,'c':56,'d':40,'e':100,'f':20}
# z=[]
# for key in my_dict:
#     x=my_dict[key]
#     z.append(x)
# max1=0
# max2=0
# max3=0
# b=[]
# for i in z:
#     if i>max1:
#         max3=max2
#         max2=max1
#         max1=i
#     elif i>max2:
#         max2=i
#     elif i>max3:
#         max3=i
# b.append(max1)
# b.append(max2)
# b.append(max3)
# print(b)

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
b.append(max1)
b.append(max2)
b.append(max3)
print(b)

