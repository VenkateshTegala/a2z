'''
Longest Consecutive Subsequence
Difficulty: Medium

Given an array arr[] of non-negative integers. Find the length of the longest sub-sequence such that elements in
the subsequence are consecutive integers, the consecutive numbers can be in any order.

Examples:
Input: arr[] = [2, 6, 1, 9, 4, 5, 3]
Output: 6
Explanation: The consecutive numbers here are 1, 2, 3, 4, 5, 6. These 6 numbers form the longest consecutive subsquence.

Input: arr[] = [1, 9, 3, 10, 4, 20, 2]
Output: 4
Explanation: 1, 2, 3, 4 is the longest consecutive subsequence.

Input: arr[] = [15, 13, 12, 14, 11, 10, 9]
Output: 7
Explanation: The longest consecutive subsequence is 9, 10, 11, 12, 13, 14, 15, which has a length of 7.

Constraints:
1 <= arr.size() <= 105
0 <= arr[i] <= 105
'''

#Better : By Sorting 
class Solution:
    def longestConsecutive(self,arr):
        #code here
        arr.sort()
        count = 1
        max_count = 0
        for i in range(len(arr) - 1):
            if arr[i] == arr[i + 1]:
                continue
            elif arr[i] + 1 == arr[i + 1]:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 1
        max_count = max(max_count, count)
        return max_count
    

