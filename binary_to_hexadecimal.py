x=int(input("Enter a number :"))
y=str(x)
for i in y:
    if i=="0" or i=="1":
        pass
    else:
        print("Entered number is not a binary number.")
        break
def hexa(a):
    if a=='10':
        return "A"
    if a=='11':
        return "B"
    if a=='12':
        return "C"
    if a=='13':
        return "D"
    if a=='14':
        return "E"
    if a=='15':
        return "F"
    else:
        return a
r=0
a=y[::-1]
for i in range(len(y)):
    f=int(a[i])*(2**i)
    r=r+f
print(r)
q=''
while r>0:
    g=str(r%16)
    t=hexa(g)
    q=q+t
    r=r//16
print(q[::-1])
