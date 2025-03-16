'''
1 2 3 4 5 
1 2 3 4
1 2 3
1 2
1
'''

for i in range(5):
    for j in range(5 - i):
        print(j + 1, end=" ")
    print()