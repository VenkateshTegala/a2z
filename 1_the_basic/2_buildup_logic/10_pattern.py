'''
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''
n = int(input())
for i in range(n):
    for j in range(i + 1):
        print("*", end=" ")
    print()
for i in range(n, n + n):
    for j in range(n + n - i - 1):
        print("*", end=" ")
    print()