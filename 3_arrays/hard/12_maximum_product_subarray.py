'''
152. Maximum Product Subarray
Medium
Given an integer array nums, find a subarray that has the largest product, and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer.

Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

Constraints:
1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any subarray of nums is guaranteed to fit in a 32-bit integer.
'''

#Brute Force: With 3 loops
#Time complexity : O(n^3)  Space complexity:O(1)
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_product = float("-inf")
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                product = 1
                for k in range(i, j + 1):
                    product *= nums[k]
                max_product = max(max_product, product)
        return max_product
    
    
    
#Better: With two loops
#Time complexity: O(n^2)  Space complexity: O(1)
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_product = float("-inf")
        for i in range(len(nums)):
            product = 1
            for j in range(i, len(nums)):
                product *= nums[j]
                max_product = max(max_product, product)

        return max_product
        
        
        
        
#Optimal: Using prefix and suffix
#Time complexity: O(2n)  Space complexity: O(1)
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix = 1
        suffix = 1
        max_product = float("-inf")
        for num in nums:
            prefix *= num
            max_product = max(max_product, prefix)
            if num == 0:
                prefix = 1
        for i in range(len(nums) - 1, -1, -1):
            suffix *= nums[i]
            max_product = max(max_product, suffix)
            if nums[i] == 0:
                suffix = 1
        return max_product



        

        