'''
560. Subarray Sum Equals K
Medium
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2

Constraints:
1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
'''


#Brute Force : With 3 loops sumation from i to j
#Time Complexity: O(n ^ 3) Space Complexity:O(1)
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        mysum = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                for l in range(i, j + 1):
                    mysum += nums[l]
                if mysum == k:
                    count += 1
                mysum = 0
        return count
    
    
    
#Better: With two loops continous sumation from i to j
#Time complexity: O(n^2)  Space complexity: O(1)
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            mysum = 0
            for j in range(i, len(nums)):
                mysum += nums[j]
                if mysum == k:
                    count += 1
        return count
        
        

#Optimal : With prefix sum(Hash Map)
#Time Complexity: O(n)  Space complexity :O(n)
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        mydict = {0 : 1}
        count = 0
        mysum = 0
        for num in nums:
            mysum += num
            if mysum - k in mydict:
                count += mydict[mysum - k]
            if mysum not in mydict:
                mydict[mysum] = 1
            else:
                mydict[mysum] += 1
        return count