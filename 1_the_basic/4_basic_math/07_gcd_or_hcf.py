#GCD or HCF

num1 = int(input())
num2 = int(input())

def highest_common_fact(num1, num2):
    if num1 == 0:
        return num2
    if num1 > num2:
        return highest_common_fact(num1 % num2, num2)
    else:
        return highest_common_fact(num2 % num1, num1)

factor = highest_common_fact(num1, num2)
print(factor)