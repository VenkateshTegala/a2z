'''
[4, 4, 4, 4, 4, 4, 4]
[4, 3, 3, 3, 3, 3, 4]
[4, 3, 2, 2, 2, 3, 4]
[4, 3, 2, 1, 2, 3, 4]
[4, 3, 2, 2, 2, 3, 4]
[4, 3, 3, 3, 3, 3, 4]
[4, 4, 4, 4, 4, 4, 4]
'''

n = int(input())
matrix = [[0] * (2*n - 1) for _ in range(2 * n -1)]
print(matrix)
for i in range(2*n - 1):
    for j in  range(2*n - 1):
        top = i
        bottom = 2*n - 2 - i
        left = j
        right = 2*n - 2 - j
        matrix[i][j] = n - min(top, bottom, right, left)
for list in matrix:
    print(list)
        