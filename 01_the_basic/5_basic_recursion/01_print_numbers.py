#printing the numbers from 1 to n
def my_recursion(num, n):
    if num == n + 1:
        return
    print(num, end=" ")
    return my_recursion(num + 1, n)

n = int(input())
my_recursion(1, n)