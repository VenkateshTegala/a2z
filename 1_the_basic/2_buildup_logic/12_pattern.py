'''
1                   1
1 2               2 1
1 2 3           3 2 1 
1 2 3 4       4 3 2 1
1 2 3 4 5   5 4 3 2 1
'''
n = int(input())
for i in range(n):
    for j in range(i + 1):
        print(j + 1, end=" ")
    for j in range(i + 1, n + n - i):
        print(" ", end=" ")
    for j in range(n + n - i, n + n + 1):
        print(n + n - j + 1, end=" ")
    print()