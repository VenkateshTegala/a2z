'''
540. Single Element in a Sorted Array
Solved
Medium
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.
Return the single element that appears only once.
Your solution must run in O(log n) time and O(1) space.

Example 1:
Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:
Input: nums = [3,3,7,7,10,11,11]
Output: 10

Constraints:
1 <= nums.length <= 105
0 <= nums[i] <= 105
'''

#Brute Force: Using xor operation
#Time complexity: O(n)  Space complexity: O(1)
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xor = 0
        for i in range(len(nums)):
            xor ^= nums[i]
        return xor
        
        
        
        
#Optimal: Using Binary Search
#Time complexity: O(logn)  Space complexity: O(1)
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[n - 1] != nums[n - 2]:
            return nums[n - 1]
        start = 1
        end = n - 2
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid - 1] != nums[mid] and nums[mid + 1] != nums[mid]:
                return nums[mid]
            elif (mid % 2 == 0 and nums[mid] == nums[mid + 1]) or (mid % 2 != 0 and nums[mid - 1] == nums[mid]):
                start = mid + 1
            else:
                end = mid - 1
        return -1
        