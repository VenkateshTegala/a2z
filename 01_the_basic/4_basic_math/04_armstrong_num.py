#An Armstrong number is a number that equals the sum of its digits, each raised to the power of the number of digits
num = int(input())
n = num
sum = 0
power = len(str(num))
while(num > 0):
    digit = num % 10
    sum += digit**power
    num = num // 10
print(n == sum)