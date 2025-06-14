'''
268. Missing Number
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Example 1:
Input: nums = [3,0,1]
Output: 2
Explanation:
n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

Example 2:
Input: nums = [0,1]
Output: 2
Explanation:
n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

Example 3:
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation:
n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.

Constraints:
n == nums.length
1 <= n <= 104
0 <= nums[i] <= n
All the numbers of nums are unique.
'''

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sum1 = n * (n + 1)/2
        sum2 = 0
        for num in nums:
            sum2 += num
        
        return sum1 - sum2

        '''
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] > -1 and nums[i] < n and nums[i] != i:
                element = nums[i]
                nums[i] = nums[element]
                nums[element] = element
            else:
                i += 1
        for i in range(n):
            if nums[i] != i:
                return i
        return n
        '''
        