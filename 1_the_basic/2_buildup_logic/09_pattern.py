'''
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * * 
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
'''

n = int(input())

#just combine upward and downward pyramid
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end=" ")
    for j in range(n - i - 1, n + i):
        print("*", end=" ")
    for j in range(n + i + 1, n + n):
        print(" ", end=" ")
    print()
    
for i in range(n - 2, -1, -1):
    for j in range(n - i - 1):
        print(" ", end=" ")
    for j in range(n - i - 1, n + i):
        print("*", end=" ")
    for j in range(n + i + 1, n + n):
        print(" ", end=" ")
    print()
