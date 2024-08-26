x=int(input("Enter a number :"))
y=str(x)
for i in y:
    if int(i)<=7:
        pass
    else:
        print("Entered number is not a binary number.")
        break
r=0
a=y[::-1]
for i in range(len(y)):
    f=int(a[i])*(8**i)
    r=r+f
print(r)
