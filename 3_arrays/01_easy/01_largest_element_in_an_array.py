
from typing import List


class Solution:
    def largest(self, arr):
        # code here
        max_element = float('-inf')
        for num in arr:
            max_element = max(max_element, num)
        return max_element



#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        arr = list(map(int, input().split()))

        obj = Solution()
        res = obj.largest(arr)

        print(res)
        print("~")

# } Driver Code Ends