class Employee:
    def Greet():
        print(f"Hello \t \n ")

    language=input(" ")

    if(language=="Python"):
        salary=120000
        print(f"Your Salary is {salary}")

    else:
        print(f"Your Language is = {language}")
    
    

yash=Employee
yash.Greet()
print(yash)
