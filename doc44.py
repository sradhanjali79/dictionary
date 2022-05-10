


# x={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
# keys=x.keys()
# for k in keys:
#     v=[x[k]]
# for i in v:
#     m=dict(zip(keys,i))
# print(m)
        
# d = {'key1': [1, 2, 3], 'key2': [4, 5, 6]}

# keys = d.keys()
# vals = zip(*[d[k] for k in keys])
# l = [dict(zip(keys, v)) for v in vals]
# print(l)
d = {'key1': [1, 2, 3], 'key2': [4, 5, 6]}
s=[dict(zip(d.keys(),i)) for i in zip(*d.values())]
print(s)
