x={"a":123,"b":{"c":10,"d":45,"e":{"f":167,"h":56}}}
z=[]
for k in x.values():
    z.append(k)
min=z[0]
max=0
for i,j in x.items():
    if type(j)==int:
        if j<min:
            min=j
        elif j>max:
            max=j
    elif type(j)==dict:
        for p,q in j.items():
            if type(q)==int:
                if q<min:
                    min=q
                elif q>max:
                    max=q
            elif type(q)==dict:
                for m,n in q.items():
                    if n<min:
                        min=n
                    elif n>max:
                        max=n
print("maximun num =",max)
print("minimun num =",min)

