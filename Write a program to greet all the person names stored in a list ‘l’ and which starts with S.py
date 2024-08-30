#Write a program to greet all the person names stored in a list ‘l’ and which starts
#with S.

p = ["Harry", "Soham", "Sachin", "Rahul"]

for name in p:
    if name.startswith('S') or name.startswith('s'):
        print("\n\n Hello", name,"\n\n")
    else:
        print(" ")
