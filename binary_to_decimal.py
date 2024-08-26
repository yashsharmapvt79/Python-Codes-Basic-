x=int(input("Enter a number :"))
y=str(x)
for i in y:
    if i=="0" or i=="1":
        r=0
        a=y[::-1]
        for i in range(len(y)):
            f=int(a[i])*(2**i)
            r=r+f
        print(r*1)
    else:
        print("Entered number is not a binary number.")


