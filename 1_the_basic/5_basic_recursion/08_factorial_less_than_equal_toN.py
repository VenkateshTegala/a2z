'''
A number n is called a factorial number if it is the factorial of a positive integer. For example, the first few factorial numbers are 1, 2, 6, 24, 120,
Given a number n, the task is to return the list/vector of the factorial numbers smaller than or equal to n.
Examples:
Input: n = 3
Output: 1 2
Explanation: The first factorial number is 1 which is less than equal to n. The second number is 2 which is less than equal to n,but the third factorial number is 6 which is greater than n. So we print only 1 and 2.
Input: n = 6
Output: 1 2 6
Explanation: The first three factorial numbers are less than equal to n but the fourth factorial number 24 is greater than n. So we print only first three factorial numbers.
'''
#User function Template for python3

class Solution:
    def factorialNumbers(self, n):
    #code here 
        result = []
        def factorial(num, factorial_value, result):
            if factorial_value > n:
                return
            result.append(factorial_value)
            factorial(num + 1, factorial_value * (num + 1), result)
        factorial(1, 1, result)
        return result
        #{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.factorialNumbers(N)
        for i in ans:
            print(i, end=" ")
        print()
        print("~")

# } Driver Code Ends