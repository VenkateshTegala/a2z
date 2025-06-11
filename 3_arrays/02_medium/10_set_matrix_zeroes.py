'''
73. Set Matrix Zeroes
Medium

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Constraints:
m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
'''

#Brute Force : If matrix contains only positives or 0's and 1's 
#Time complextiy is O(n^3)  Space complexity : O(1)
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    for k in range(len(matrix)):
                        if matrix[k][j] != 0:
                            matrix[k][j] = -1
                    for k in range(len(matrix[0])):
                        if matrix[i][k] != 0:
                            matrix[i][k] = -1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == -1:
                    matrix[i][j] = 0
        
        
#Better with marking row and col indices
#Time complexity: O(n^2)  Space complexity: O(m + n)
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row_list = [0] * len(matrix)
        col_list = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row_list[i] = 1
                    col_list[j] = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if row_list[i] == 1 or col_list[j] == 1:
                    matrix[i][j] = 0
                    
#Optimal : Without extra space
#By considering the first row and first column to store
#Time complexity: O(2*n^2)  Space complexity: O(1) (one variable)
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        j0 = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    if j != 0:
                        matrix[0][j] = 0
                    else:
                        j0 = 0
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        if matrix[0][0] == 0:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        if j0 == 0:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        

