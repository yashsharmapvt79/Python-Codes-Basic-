'''
#Q1~Factorial of a Number
a=int(input('Enter The Number of Which You want to find Factorial : '))
w=1
for i in range(1,a+1):
    w=w*i
print('So The Factorial of',a,'= ',w)


#Q2~Program to Display the multiplication Table
b=int(input('ENTER WHICH TABLE YOU WANT OT DISPLAY : '))
for i in range(0,10,1):
    i+=1
    k=b*i
    print(b,'*',i,'=',k)
'''

#Q3~Program to Print the Fibonacci sequence
n=int(input("Enter no. of terms :"))
d=0
e=1
for i in range(n):
    c=d+e
    print(d,end=",")
    d=e
    e=c
print()
print('--------------------------------------------------------------------------------')
print('CODING DONE BY YASH SHARMA !!!!!!!!')  
print('--------------------------------------------------------------------------------')
print('QUESTIONS ARE DONE IN SEQUENCES')
