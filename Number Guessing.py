import random
i=int(input("\n\nEnter The Range of Choosing Numbers by System : "))
print("\n")
t=int(input("\n\nEnter The Number : "))

r=random.randint(1,i)
if(t==r):
    print("\nYou Guessed it Right!!!!\n\n\n")
else:
    print("Sorry!! Try Again")