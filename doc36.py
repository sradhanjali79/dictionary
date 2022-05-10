x={'key1': 1, 'key2': 3, 'key3': 2}
y={'key1': 1, 'key2': 2}
for i,j in x.items():
    if i in y and x[i]==y[i]:
        print(i,":",j,"is present in both x and y") 
