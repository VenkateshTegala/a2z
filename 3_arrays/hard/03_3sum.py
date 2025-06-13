'''
15. 3Sum
Solved
Medium
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:
3 <= nums.length <= 3000
-105 <= nums[i] <= 105
'''

#Brute Force: With traditional approach 
#Time complexity: O(n^3) + O(3log3) + O(m) m=no of triplets ---> O(n^3 * m)  Space complexity: O(n^3) in worst case, if all the elements can form tripletss
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = [nums[i], nums[j], nums[k]]
                        triplet.sort()
                        if triplet not in result:
                            result.append(triplet)
        return result

                        
        
#Better: By using HashMap
#Time complexity: O(n^2) + O(n) (worst hash) + O(n) (set) --> O(n^2)  Space complexity: O(n) + O(n^2) in worst case if all elements have triplets
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result_set = set()
        for i in range(len(nums)):
            mydict = {}
            for j in range(i + 1, len(nums)):
                required = -(nums[i] + nums[j])
                if required in mydict:
                    triplet = [nums[i], nums[j], required]
                    triplet.sort()
                    result_set.add(tuple(triplet))
                mydict[nums[j]] = 1
        return [triplet for triplet in result_set]
    
    
    
#Optimal: By sorting and two pointers
#Time complexity: O(nlogn) + O(n^2) --> O(n^2)  Space complexity: O(1)
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                mysum = nums[i] + nums[j] + nums[k]
                if mysum < 0:
                    j += 1
                elif mysum > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        return result


        


        