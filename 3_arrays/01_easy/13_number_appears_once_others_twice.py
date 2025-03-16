'''
136. Single Number
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1

Constraints:
1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.
'''

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #doing xor bitwise leads to zero for duplicates
        xor = 0
        for num in nums:
            xor = xor^num
            #print(xor)
        return xor

        '''
        frequency={}
        for num in nums:
            if num in frequency:
                frequency[num]+=1
            else:
                frequency[num]=1
        for num in frequency:
            if frequency[num]==1:
                return num
        '''
        