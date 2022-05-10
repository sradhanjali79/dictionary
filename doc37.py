dic={'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}
for value in dic.values():
    print(value[4])
for key,value in dic.items():
    print(key,"has value",value)