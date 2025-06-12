'''
229. Majority Element II
Solved
Medium
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Example 1:
Input: nums = [3,2,3]
Output: [3]

Example 2:
Input: nums = [1]
Output: [1]

Example 3:
Input: nums = [1,2]
Output: [1,2]

Constraints:
1 <= nums.length <= 5 * 104
-109 <= nums[i] <= 109
'''


#Brute Force: Roughly O(n^2) a traditional method
#Time complexity: O(n^2) + O(2) --> O(n^2)  Space complexity:O(2)
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[j] == nums[i]:
                    count += 1
                if count >= n//3 + 1 and nums[i] not in result:
                    result.append(nums[i])
                    break
        result.sort()
        return result




#Better: By using HashMap
#Time complexity: O(n) + O(k) + O(2log2) --> O(n)  Space complexity: O(n) in worst of HashMap
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = []
        mydict = {}
        for num in nums:
            if num in mydict:
                mydict[num] += 1
            else:
                mydict[num] = 1
        for key in mydict:
            if mydict[key] > n//3:
                result.append(key)
        result.sort()
        return result
    
    
    

#Optimal: With Boyer_Morre Voting Algorithm
#Time complexity: O(n) + O(n) + O(2log2) --> O(n)  Spacr complexity : O(1)
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = []
        count_1 = 0
        count_2 = 0
        element_1 = 0
        element_2 = 0
        for i in range(len(nums)):
            if count_1 == 0 and nums[i] != element_2: 
                element_1 = nums[i]
                count_1 += 1
            elif count_2 == 0 and nums[i] != element_1:
                element_2 = nums[i]
                count_2 += 1
            elif nums[i] == element_1:
                count_1 += 1
            elif nums[i] == element_2:
                count_2 += 1
            else:
                count_1 -= 1
                count_2 -= 1
        count_1 = 0
        count_2 = 0
        for num in nums:
            if num == element_1:
                count_1 += 1
            elif num == element_2:
                count_2 += 1
        if count_1 > n//3:
            result.append(element_1)
        if count_2 > n//3:
            result.append(element_2)
        result.sort()
        return result
        
        