'''
Count Subarrays with given XOR
Difficulty: Medium
Given an array of integers arr[] and a number k, count the number of subarrays having XOR of their elements as k.

Examples: 

Input: arr[] = [4, 2, 2, 6, 4], k = 6
Output: 4
Explanation: The subarrays having XOR of their elements as 6 are [4, 2], [4, 2, 2, 6, 4], [2, 2, 6], and [6]. Hence, the answer is 4.

Input: arr[] = [5, 6, 7, 8, 9], k = 5
Output: 2
Explanation: The subarrays having XOR of their elements as 5 are [5] and [5, 6, 7, 8, 9]. Hence, the answer is 2.

Input: arr[] = [1, 1, 1, 1], k = 0
Output: 4
Explanation: The subarrays are [1, 1], [1, 1], [1, 1] and [1, 1, 1, 1].

Constraints:
1 ≤ arr.size() ≤ 105
0 ≤ arr[i] ≤105
0 ≤ k ≤ 105
'''

#Brute Force: With pointers
#Time complexity: O(n^3)  Space complexity: O(1)
class Solution:
    def subarrayXor(self, arr, k):
        # code here
        count = 0
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                xor = 0
                for l in range(i, j + 1):
                    xor ^= arr[l]
                if xor == k:
                    count += 1
        return count
    
    
    
#Better: By add or xor
#Time complexity: O(n^2)  Space complexity: O(1)
class Solution:
    def subarrayXor(self, arr, k):
        # code here
        count = 0
        for i in range(len(arr)):
            xor = 0
            for j in range(i, len(arr)):
                xor ^= arr[j]
                if xor == k:
                    count += 1
        return count
                    
                    
                    
                    
#Optimal: zWith prefix xor using hashmap
#Time complexity: O(n)  Space complexity; O(n) in worst case for HashMap
class Solution:
    def subarrayXor(self, arr, k):
        # code here
        mydict = {}
        xor = 0
        count = 0
        for i in range(len(arr)):
            xor ^= arr[i]
            if xor == k:
                count += 1
            if xor^k in mydict:
                count += mydict[xor^k]
            if xor in mydict:
                mydict[xor] += 1
            else:
                mydict[xor] = 1
        return count
                    