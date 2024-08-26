# function to find number of lower and upper case letters in a string
def no(B):
    s={'UPPER CASE':0}
    o={'LOWER CASE':0}
    for i in (B):
        if i.isupper():
            s['UPPER CASE']+=1
        elif i.islower():
            o['LOWER CASE']+=1
        else:
            pass
    print('REAL TYPED STRING : ',B)#TYPING ORIGINAL STRING
    print('THE NUMBER OF UPPER CASE LETTERS IS: ',s['UPPER CASE'])#GIVE NUMBER OF UPPERCASE LETTERS
    print('THE NUMBER OF LOWER CASE LETTERS IS: ',o['LOWER CASE'])#GIVE NUMBER OF LOWERCASE LETTERS
B=str(input('ENTER THE SENTENCE PLEASE : '))
no(B)
print('CODING DESIGNED BY YASH SHARMA (PCM)!!!')
