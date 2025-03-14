'''
name = "Venky"
n = int(input())
check = 1
def printName(n, check):
    if check > n:
        return
    print(name)
    check += 1
    printName(n, check)
printName(n, check)
'''

#disturbing approach
print("Enter your name :")
name = str(input())
print("enter no of times :")
n = int(input())
def print_Name(n):
    if n == 0:
        return
    n -= 1
    print_Name(n)
    print(name)
print_Name(n)