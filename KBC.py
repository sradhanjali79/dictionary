question=["What is the capital of india ?" ,"How many states are there in india ?","What is the capital of odisha"]
option=[["Bbsr","Delhi","karnataka","Panjab"],["28","29","30","31"],["Cuttack","Jajpur","Bhubaneswar","Bhadrak"]]
solution=[2,1,3]
option2=[["Delhi","Bbsr"],["29","28"],["jajpur","Bhubaneswar"]]
solution2=[1,2,2]
i=0
count=0
while i<len(question):
    print("Q",i+1,question[i])
    j=0
    while j<len(option[i]):
        print(j+1,option[i][j])
        j=j+1
    user=int(input("enter any number"))
    if user==solution[i]:
        print("congratulation")
    elif user==5050:
        if count==0:
            k=0
            while k<len(option2[i]):
                print(k+1,option2[i][k])
                k=k+1
            count=count+1
            user2=int(input("enter any number"))
            if user2==solution2[i]:
                print("winner")
            else:
                print("wrong")
        else:
            print("sorry already used")
            num=int(input("enter any number"))
            if num==solution[i]:
                print("correct answer")
            else:
                print("wrong answer")
                break
    else:
        print("galat hai")
        break
    i=i+1
