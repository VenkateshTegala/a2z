'''
Find Kth Rotation
Difficulty: Easy
Given an increasing sorted rotated array arr of distinct integers. The array is right-rotated k times. Find the value of k.
Let's suppose we have an array arr = [2, 4, 6, 9], so if we rotate it by 2 times so that it will look like this:
After 1st Rotation : [9, 2, 4, 6]
After 2nd Rotation : [6, 9, 2, 4]

Examples:
Input: arr = [5, 1, 2, 3, 4]
Output: 1
Explanation: The given array is 5 1 2 3 4. The original sorted array is 1 2 3 4 5. We can see that the array was rotated 1 times to the right.

Input: arr = [1, 2, 3, 4, 5]
Output: 0
Explanation: The given array is not rotated.
Expected Time Complexity: O(log(n))
Expected Auxiliary Space: O(1)

Constraints:
1 <= n <=105
1 <= arri <= 107
'''

#Optimal: USing Binary Search 
#Time complexity: O(logn)  Space complexity: O(1)
class Solution:
    def findKRotation(self, arr):
        # code here
        start = 0
        end = len(arr) - 1
        min_index = -1
        min_element = float("inf")
        while start <= end:
            mid = start + (end - start) // 2
            if arr[start] <= arr[mid]:
                if arr[start] < min_element:
                    min_element = arr[start]
                    min_index = start
                start = mid + 1
            else:
                if arr[mid] < min_element:
                    min_element = arr[mid]
                    min_index = mid
                end = mid - 1
        return min_index
        