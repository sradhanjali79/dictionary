x={"a":123,"b":{"c":100,"d":45,"e":{"f":167,"h":56,"s":200}}}
max=0
for i,j in x.items():
    if type(j)==int:
        if j>max:
            max=j
    elif type(j)==dict:
        for p,q in j.items():
            if type(q)==int:
                if q>max:
                    max=q
            elif type(q)==dict:
                for m,n in q.items():
                    if n>max:
                        max=n
print("maximun num =",max)