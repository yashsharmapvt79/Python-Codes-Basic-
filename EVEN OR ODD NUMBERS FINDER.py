
a=int(input("Enter The Number : "))
if a%2==0 or a==2:
    print(a,"The Number Is Even")
elif a%3==0 or a==3:
    print(a,"The Number Is Odd")
elif a==1:
        print("Value Is 1")
else:
        print(a,"Is The Prime Number .")

'''
# Python program to draw star
# using Turtle Programming
import turtle 

star = turtle.Turtle()
star.color('green')
star.fillcolor('yellow')
turtle.Screen().bgcolor('black')
star.begin_fill()
for i in range(20):
        star.forward(100+1)
        star.right(144)
star.end_fil()
turtle.done()
'''
