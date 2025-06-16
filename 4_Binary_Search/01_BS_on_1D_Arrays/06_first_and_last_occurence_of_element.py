'''
34. Find First and Last Position of Element in Sorted Array
Solved
Medium
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]

Constraints:
0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
'''

#Brute Force: Using Linear Search
#Time Complexity: O(n)  Space complexity: O(1)
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mylist = []
        for i in range(len(nums)):
            if nums[i] == target:
                mylist.append(i)
                for j in range(i, len(nums)):
                    if nums[j] != target:
                        mylist.append(j - 1)
                        return mylist
                mylist.append(len(nums) - 1)
                return mylist
        return [-1, -1]
        
        
        
        
#Optimal: Using Binary Search
#Time complexity: O(2logn) Space complexity: O(1)
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lower = - 1
        upper = -1
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] >= target:
                if nums[mid] == target:
                    lower = mid
                end = mid - 1
            else:
                start = mid + 1
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] <= target:
                if nums[mid] == target:
                    upper = mid
                start = mid + 1
            else:
                end = mid - 1
        if lower == -1 or upper == -1:
            return [-1, -1]
        return [lower, upper]