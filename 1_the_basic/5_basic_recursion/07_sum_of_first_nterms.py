'''
Given an integer n, calculate the sum of series 13 + 23 + 33 + 43 + … till n-th term.
Examples:
Input: n = 5
Output: 225
Explanation: 13 + 23 + 33 + 43 + 53 = 225
Input: n = 7
Output: 784
Explanation: 13 + 23 + 33 + 43 + 53 + 63 + 73 = 784
Constraints:
1 <= n <= 200 
'''
#User function Template for python3

class Solution:
    def sumOfSeries(self,n):
        #code here
        def mysum(n):
            if n == 0:
                return 0
            return n**3 + mysum(n - 1)
        return mysum(n)
            
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        ob=Solution()
        print(ob.sumOfSeries(N)) 
        print("~")
# } Driver Code Ends