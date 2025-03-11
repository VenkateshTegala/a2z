'''
A B C D E
A B C D
A B C
A B
A
'''
n = int(input())
for i in range(n - 1, -1, -1):
    for j in range(i + 1):
        print(chr(65 + j), end=" ")
    print()