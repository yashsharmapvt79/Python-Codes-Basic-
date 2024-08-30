import random

p=random.choice([1,0,-1])
ch=int(input("ENTER YOUR CHOICE \n 1 for Snake :  \n -1 for Water : \n 0 for Gun : "))

if(p==1 and ch==1):
    print("Its A Draw")

elif(p==1 and ch==-1):
    print("You Lost")

elif(p==1 and ch==0):
    print("You Won")

elif(p==0 and ch==1):
    print("You Lost")

elif(p==0 and ch==-1):
    print("You Won")

elif(p==0 and ch==0):
    print("Its a Draw")

elif(p==-1 and ch==1):
    print("You Won")

elif(p==-1 and ch==-1):
    print("Its a Draw")

elif(p==-1 and ch==0):
    print("You Lost")

else:
    print(":::::: Error While choosing the Values ::::::  ")