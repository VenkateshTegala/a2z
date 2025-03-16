'''
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
'''
n = int(input())
for i in range(n - 1, -1, -1):
    for j in range(n - i - 1):
        print(" ", end=" ")
    for j in range(n - i - 1, n + i):
        print("*", end=" ")
    for j in range(n + i + 1, n + n):
        print(" ", end=" ")
    print()