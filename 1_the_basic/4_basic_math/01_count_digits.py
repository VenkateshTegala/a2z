print("Enter a number :")
num = int(input())
count = 0
while(num > 0): 
    digit = num % 10
    print(digit)
    count += 1
    num = num // 10
print(f"Total no of digits : {count}")

'''
else we can do like
import math
digits = int(math.log10(num)) + 1
'''
