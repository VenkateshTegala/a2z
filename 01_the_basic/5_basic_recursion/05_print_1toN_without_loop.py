'''
Print numbers from 1 to n without the help of loops. You only need to complete the function printNos() that takes n as a parameter and prints the number from 1 to n recursively.
Note: Don't print any newline, it will be added by the driver code.
Examples:
Input: n = 10
Output: 1 2 3 4 5 6 7 8 9 10
Input: n = 5
Output: 1 2 3 4 5
'''
#User function Template for python3

class Solution:    
    #Complete this function
    def printNos(self,n):
        #Your code here
        if n == 0:
            return 
        self.printNos(n - 1)
        print(n, end = " ")


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():

    T = int(input())

    while (T > 0):

        N = int(input())

        ob = Solution()

        ob.printNos(N)
        print()
        T -= 1

        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends