'''
Merge Without Extra Space
Difficulty: Medium
Given two sorted arrays a[] and b[] of size n and m respectively, the task is to merge them in sorted order without using any extra space. Modify a[] so that it contains the first n elements and modify b[] so that it contains the last m elements.

Examples:
Input: a[] = [2, 4, 7, 10], b[] = [2, 3]
Output:
2 2 3 4
7 10
Explanation: After merging the two non-decreasing arrays, we get, 2 2 3 4 7 10

Input: a[] = [1, 5, 9, 10, 15, 20], b[] = [2, 3, 8, 13]
Output:
1 2 3 5 8 9
10 13 15 20
Explanation: After merging two sorted arrays we get 1 2 3 5 8 9 10 13 15 20.
I
nput: a[] = [0, 1], b[] = [2, 3]
Output:
0 1
2 3
Explanation: After merging two sorted arrays we get 0 1 2 3.

Constraints:
1 <= a.size(), b.size() <= 105
0 <= a[i], b[i] <= 107
'''

#Brute Force: By placing values in a sorted way in another list
#Time complexity: 2(O(m) + O(n))  Space complexity: O(m + n)
class Solution:
    def mergeArrays(self, a, b):
        # code here
        result = []
        p1 = 0
        p2 = 0
        while p1 < len(a) and p2 < len(b):
            if a[p1] < b[p2]:
                result.append(a[p1])
                p1 +=1
            elif b[p2] < a[p1]:
                result.append(b[p2])
                p2 +=1
            else:
                result.append(a[p1])
                result.append(b[p2])
                p1 +=1
                p2 +=1
        while p1 != len(a):
            result.append(a[p1])
            p1 +=1
        while p2 != len(b):
            result.append(b[p2])
            p2 +=1
        
        #Copying elements
        for i in range(len(a)):
            a[i] = result[i]
        for i in range(len(a), len(result)):
            b[i - len(a)] = result[i]
            
            
            
#Better: By swapping and sorting, check it
#Time complexity: O(min(m or n)) + O(mlogn) + O(nlogn)  Space complexity: O(1)
class Solution:
    def mergeArrays(self, a, b):
        # code here
        left = len(a) - 1
        right = 0
        while left > 0 and right < len(b):
            if b[right] < a[left]:
                b[right], a[left] = a[left], b[right]
            left -= 1
            right += 1
        a.sort()
        b.sort()
        
        
        
        
#Optimal: Using gap method (By Shell Sort)
#Time complexity: O(m + n)log(m + n)  Space complexity: O(1)
class Solution:
    def mergeArrays(self, a, b):
        # code here
        gap = ((len(a) + len(b)) + 1) // 2
        right = gap
        while gap > 0:
            left = 0
            right = gap
            while right < (len(a) + len(b)):
                if left < len(a) and right >= len(a):
                    if b[right - len(a)] < a[left]:
                        b[right - len(a)], a[left] = a[left], b[right - len(a)]
                elif left >= len(a):
                    if b[right - len(a)] < b[left - len(a)]:
                        b[right - len(a)], b[left - len(a)] = b[left - len(a)], b[right - len(a)]
                else:
                    if a[right] < a[left]:
                        a[right], a[left] = a[left], a[right]
                left += 1
                right += 1
            if gap == 1:
                gap = 0
            else:
                gap = (gap + 1) // 2
            
                