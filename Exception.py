i=input("Enter Value : ")

try:
    for k in range(11):
        i=int(i)
        print(f"{i} * {k} = {i}*{k}")
except Exception as e:
    print("\n")
    print("Error Is = ",e)