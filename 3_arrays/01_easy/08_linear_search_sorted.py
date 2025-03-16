'''
Sorted Array Search
Difficulty: BasicAccuracy: 48.03%Submissions: 342K+Points: 1Average Time: 20m
Given an array, arr[] sorted in ascending order and an integer k. Return true if k is present in the array, otherwise, false.
Examples:

Input: arr[] = [1, 2, 3, 4, 6], k = 6
Output: true
Exlpanation: Since, 6 is present in the array at index 4 (0-based indexing), output is true.

Input: arr[] = [1, 2, 4, 5, 6], k = 3
Output: false
Exlpanation: Since, 3 is not present in the array, output is false.

Input: arr[] = [2, 3, 5, 6], k = 1
Output: false

Constraints:
1 <= arr.size() <= 106
1 <= k <= 106
1 <= arr[i] <= 106
'''

#User function Template for python3

class Solution:
    ##Complete this function
    def searchInSorted(self,arr, k):
        #Your code here
        for num in arr:
            if num == k:
                return True
        return False

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        A = [int(x) for x in input().strip().split()]
        k = int(input())
        ob = Solution()
        print("true" if ob.searchInSorted(A, k) else "false")
        print("~")

# } Driver Code Ends