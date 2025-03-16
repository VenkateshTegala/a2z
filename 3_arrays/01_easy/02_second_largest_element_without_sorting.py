#User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        max_element = -1
        sec_max = -1
        for num in arr:
            if num > max_element:
                sec_max = max_element
                max_element = num
            elif num > sec_max and num != max_element:
                    sec_max = num
        
        return sec_max

#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
        print("~")
# } Driver Code Ends