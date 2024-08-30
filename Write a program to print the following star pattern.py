'''
Write a program to print the following star pattern.
*
***
***** for n = 3

'''

def print_star_pattern(n):
    for i in range(n):
        stars = '*' * (2 * i + 1)
        print(stars)
n=3
print("\n\n")
print_star_pattern(n)
print("\n\n")
