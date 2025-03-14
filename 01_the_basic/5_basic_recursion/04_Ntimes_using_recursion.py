'''
Print GFG n times without the loop.
Example:
Input:
5
Output:
GFG GFG GFG GFG GFG
Your Task:
This is a function problem. You only need to complete the function printGfg() that takes N as parameter and prints N times GFG recursively. Don't print newline, it will be added by the driver code.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N) (Recursive).
'''

#User function Template for python3

class Solution:
    def printGfg(self, n):
        # Code here
        if n == 0:
            return 
        n -= 1
        self.printGfg(n)
        print("GFG", end = " ")
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printGfg(N)
        print()
        print("~")
# } Driver Code Ends