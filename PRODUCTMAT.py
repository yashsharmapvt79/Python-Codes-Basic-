#CREATE MATRIX-1
print('Now type 1st Matrix')
M1=[]
r1=int(input("Enter number of rows: "))
c1=int(input("Enter number of columns: "))
print("Enter the entries: ")
for i in range(r1):
    A=[]                                            
    for j in range(c1):
        A.append(int(input("Enter Input: ")))
    M1.append(A)

print(M1)

#CREATE MATRIX-2
print('Now type 2nd Matrix')
M2=[]
r2=int(input("Enter number of rows: "))
c2=int(input("Enter number of columns: "))
print("Enter the entries: ")

for i in range(r2):
    A=[]
    for j in range(c2):
        A.append(int(input("Enter Input: ")))
    M2.append(A)
print(M2)

#PRODUCT MATRIX

if c1==r2:
    Pmatrix = []
    for a in range(r1):
        M = []
        for i in range(c2):
            res = 0
            for j in range(c1):
                res=res+ M1[a][j] * M2[j][i]
            M.append(res)
        Pmatrix.append(M)
    print(Pmatrix)
else:
    print("Matrix Product is not possible")
print('want to have this again : ')
