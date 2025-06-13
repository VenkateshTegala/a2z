'''
18. 4Sum
Medium
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]

Constraints:
1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
'''

#Brute Force: Traditional approach
#Time complexity: O( n^4) + O(k) Space complexity:O(k) for set + O(n^3) in worst if all can form quadruplet.
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        mysum = 0
        result = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                    for k in range(j + 1, len(nums)):
                        mysum = 0
                        for l in range(k + 1, len(nums)):
                            mysum = nums[i] + nums[j] + nums[k] + nums[l]
                            if mysum == target:
                                result.add(tuple([nums[i], nums[j], nums[k], nums[l]]))
        return [list(quadruplet) for quadruplet in result]
        
        
        
        
#Better: By using HashMap
#Time Complexity: O(n^3) + O(n) for hashmap  + O(n) to convert set to list   Space complexity: O(k) where k is unique quadruplets
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        myset = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                mydict = {}
                for k in range(j + 1, len(nums)):
                    required = target - (nums[i] + nums[j] + nums[k])
                    if required in mydict:
                        myset.add(tuple(sorted([nums[i], nums[j], nums[k], required])))
                    else:
                        mydict[nums[k]] = 1
        return [list(quad) for quad in myset]




#Optimal: Using two pointers
#Time complexity: O(n^3) in worst case  Space complexity: O(k) where k is the no of quadruplets
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        myset = set()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                k = j + 1
                l = len(nums) - 1
                while k < l:
                    mysum = nums[i] + nums[j] + nums[k] + nums[l]
                    if mysum < target:
                        k += 1
                    elif mysum > target:
                        l -= 1
                    else:
                        myset.add(tuple(sorted([nums[i], nums[j], nums[k], nums[l]])))
                        k += 1
                        l -= 1
                        while k < l and nums[k] == nums[k - 1]:
                            k += 1
                        while k < l and nums[l] == nums[l + 1]:
                            l -= 1
        return [list(quad) for quad in myset]

        
        