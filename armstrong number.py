x=int(input("Enter a number :"))
a,b=str(x),x
q=0
for i in range(len(a)):
    r=x%10
    q=q+(r**len(a))
    x=x//10
if b==q:
    print("Yes, it is a armstrong.")
else:
    print("No, it is not a armstrong.")
