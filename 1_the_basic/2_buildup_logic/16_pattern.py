'''
A
B B
C C C
D D D D
E E E E E
'''
n = int(input())
for i in range(n):
    for j in range(i + 1):
        print(chr(65 + i), end=" ")
    print()