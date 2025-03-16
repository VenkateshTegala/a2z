'''
Union of 2 Sorted with Duplicates
Difficulty: MediumAccuracy: 31.39%Submissions: 431K+Points: 4Average Time: 20m
Given two sorted arrays a[] and b[], where each array may contain duplicate elements , the task is to return the elements in the union of the two arrays in sorted order.
Union of two arrays can be defined as the set containing distinct common elements that are present in either of the arrays.

Examples:
Input: a[] = [1, 2, 3, 4, 5], b[] = [1, 2, 3, 6, 7]
Output: 1 2 3 4 5 6 7
Explanation: Distinct elements including both the arrays are: 1 2 3 4 5 6 7.

Input: a[] = [2, 2, 3, 4, 5], b[] = [1, 1, 2, 3, 4]
Output: 1 2 3 4 5
Explanation: Distinct elements including both the arrays are: 1 2 3 4 5.

Input: a[] = [1, 1, 1, 1, 1], b[] = [2, 2, 2, 2, 2]
Output: 1 2
Explanation: Distinct elements including both the arrays are: 1 2.

Constraints:
1  <=  a.size(), b.size()  <=  105
-109  <=  a[i] , b[i]  <=  109
'''

#User function Template for python3

class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,a,b):
        # code here 
        mylist = []
        i = 0
        j = 0
        while(i < len(a) and j < len(b)):
            if a[i] < b[j]:
                if not mylist or mylist[-1] != a[i]:
                    mylist.append(a[i])
                i += 1
            elif a[i] > b[j]:
                if not mylist or mylist[-1] != b[j]:
                    mylist.append(b[j])
                j += 1
            else:
                if not mylist or mylist[-1] != a[i]:
                    mylist.append(a[i])
                i ++ 1
                j += 1
        while(i < len(a)):
            if mylist[-1] != a[i]:
                mylist.append(a[i])
            i += 1
        while(j < len(b)):
            if mylist[-1] != b[i]:
                mylist.append(b[i])
            j += 1
        return mylist
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Contributed by : Nagendra Jha
# Modified by : Sagar Gupta

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        a = list(map(int, input().strip().split()))
        b = list(map(int, input().strip().split()))
        ob = Solution()
        li = ob.findUnion(a, b)
        for val in li:
            print(val, end=' ')
        print()
        print("~")

# } Driver Code Ends