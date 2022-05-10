x=[41,500,76,87,98,107]
dic={}
for i in x:
    p=""
    d=str(i)
    for j in d: 
        if j=="1":
            p=p+"one "
        elif j=="2":
            p=p+"two "
        elif j=="3":
            p=p+"three "
        elif j=="4":
            p=p+"four "
        elif j=="5":
            p=p+"five "
        elif j=="6":
            p=p+"six "
        elif j=="7":
            p=p+"seven "
        elif j=="8":
            p=p+"eight "
        elif j=="9":
            p=p+"nine "
        elif j=="0":
            p=p+"zero "    
    dic[i]=p
print(dic)