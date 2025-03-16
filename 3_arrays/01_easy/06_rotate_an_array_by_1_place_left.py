print("Enter the list elements: ")
mylist = list(map(int, input().split()))
print("The no of times to be rotated : ")
k = int(input())
print("The reversed list is :")
n = len(mylist)
k = k % n 
result = [0] * n
for i in range(n):
    result[(i + k) % n] = mylist[i]
print(result)

