dict1 =  {'Alex': ['subj1', 'subj2', 'subj3'],'David': ['subj1', 'subj2']}
count=0
for key in dict1:
    x=dict1[key]
    for i in x:
        count+=1
print(count)

