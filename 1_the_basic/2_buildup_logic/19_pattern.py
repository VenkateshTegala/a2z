n = 7
k = 4
while(n > 0):
    for i in range(n):
        for j in  range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print(k, end=" ")
        print()
    k -= 1
    n -= 2