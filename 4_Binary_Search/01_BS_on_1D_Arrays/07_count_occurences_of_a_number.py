'''
Number of occurrence
Difficulty: Easy
Given a sorted array, arr[] and a number target, you need to find the number of occurrences of target in arr[]. 

Examples :
Input: arr[] = [1, 1, 2, 2, 2, 2, 3], target = 2
Output: 4
Explanation: target = 2 occurs 4 times in the given array so the output is 4.

Input: arr[] = [1, 1, 2, 2, 2, 2, 3], target = 4
Output: 0
Explanation: target = 4 is not present in the given array so the output is 0.

Input: arr[] = [8, 9, 10, 12, 12, 12], target = 12
Output: 3
Explanation: target = 12 occurs 3 times in the given array so the output is 3.

Constraints:
1 ≤ arr.size() ≤ 106
1 ≤ arr[i] ≤ 106
1 ≤ target ≤ 106
'''

#Brute Force: Using linear search
#Time complexity: O(n)  Space complexity: O(1)
class Solution:
    def countFreq(self, arr, target):
        #code here
        count = 0
        for i in range(len(arr)):
            if arr[i] == target:
                for j in range(i, len(arr)):
                    if arr[j] == target:
                        count += 1
                    else:
                        break
                break
        return count





#Optimal: Using Binary search
#Time complexity: O(2logn)  Space complexity: O(1)
class Solution:
    def countFreq(self, arr, target):
        #code here
        start = 0
        end = len(arr) - 1
        lower = -1
        upper = len(arr) 
        while start <= end:
            mid = start + (end - start) // 2
            if arr[mid] >= target:
                if arr[mid] == target:
                    lower = mid 
                end = mid - 1
            else:
                start = mid + 1
        start = 0
        end = len(arr) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if arr[mid] <= target:
                if arr[mid] == target:
                    upper = mid
                start = mid + 1
            else:
                end = mid - 1
        if lower != -1 and upper != len(arr):
            return upper - lower + 1
        return 0
                