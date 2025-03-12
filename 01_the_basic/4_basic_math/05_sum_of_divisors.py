#User function Template for python3


class Solution:
    def sumOfDivisors(self, n):
        #code here 
        j = 1
        sum = 0
        for j in range(1, n + 1):
            for i in range(1,int(j**0.5) + 1):
                if (j % i == 0):
                    sum += i
                if i != j//i:
                    sum += j//i
        return sum
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.sumOfDivisors(N)
        print(ans)
        print("~")

# } Driver Code Ends