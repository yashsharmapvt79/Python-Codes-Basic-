x=int(input("Enter a number :"))
a,b=str(x),x
r=0
for i in range(1,x):
    if x%i==0:
        r=r+i
if r==x:
    print("Yes, it is a perfect number.")
else:
    print("No, it is not a perfect number.")
