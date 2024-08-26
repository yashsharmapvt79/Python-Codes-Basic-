
# Create A = [[1, 4, 5, 12],[-5, 8, 9, 0],[-6, 7, 11, 19]]
"""
1   4   5   12
-5  8   9    0
-6  7   11  19
"""
M=[]
r=int(input("Enter number of rows: "))
c=int(input("Enter number of columns: "))
print("Enter the entries: ")

for i in range(r):
    A=[]
    for j in range(c):
        A.append(int(input("Enter Input: ")))
    M.append(A)

print(M)
p=int(input("WANT TO DO THIS AGAIN ?? (if yes press 1 , if no then press 2)"))
if p==1:
    M=[]
    r=int(input("Enter number of rows: "))
    c=int(input("Enter number of columns: "))
    print("Enter the entries: ")

    for i in range(r):
        A=[]
        for j in range(c):
            A.append(int(input("Enter Input: ")))
        M.append(A)
elif p==2:
    print("THANKS FOR USING !!! ")
print("press any key to exit")
exit
