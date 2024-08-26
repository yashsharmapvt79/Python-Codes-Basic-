a=int(input('Enter 1st Number : '))
b=int(input('Enter 2nd Number : '))
print("WHAT YOU WANT TO DO :")
print("press 1 for ADDITION")
print("press 2 for SUBTRACTION")
print("press 3 for MULTIPLICATION")
print("press 4 for DIVISION")
print("press 5 for SQ. ROOT")
print("press 6 for CUBIC ROOT")
print("press 7 for SQUARING")
print("press 8 for CUBING")
print("press 9 for EXPONENTS ")
p=int(input("SO WHAT DID YOU DECIDE : "))
if p==1:
    w=a+b
    print(w)
elif p==2:
    if a>b:
        dif=(a-b)
        print(" ",dif)
    else:
        dif=(b-a)
        print(" ",dif)
elif p==3:
    mul=(a*b)
    print(" ",mul)
elif p==4:
    if a>b:
        div=a/b
        print(" ",div)
    elif b>a:
        div=b/a
        print(" ", div)
elif p==5:
    sqt=((a)**1/2)
    print(sqt)
    sqt1=((b)**1/2)
    print(sqt1)
elif p==6:
    cub=((a)**(1/3))
    print(cub)
    cub1=((b)**(1/3))
    print(cub1)
elif p==7 :
    sr=(a*a)
    print(sr)
    sr1=(b*b)
    print(sr1)
elif p==8:
    cb=(a*a*a)
    print(cb)
    cb1=(b*b*b)
    print(cb1)
elif p==9:
    z=input('Which Number Is Base : ')
    if z==a:
        u=a**(b)
        print(u)
    else:
        o=b**(a)
        print(o)
