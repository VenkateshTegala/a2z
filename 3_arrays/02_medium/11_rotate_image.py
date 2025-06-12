'''
48. Rotate Image
Medium
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

Constraints:
n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
'''

#Brute Force: With Creating of new matrix then copying in org matrix
#Time Complexity: O(2 * n^2)  Space Complexity: O(m*n)
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        result = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        k = len(matrix[0]) - 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                result[j][k] = matrix[i][j]
            k -= 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = result[i][j]
        
        
        
#Optimal: By transpose and reversing every row 
#Time complexity: O(n(n - 1)/2) + O(n) --> O(n^2)  Space complexity: O(1)
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix[0])):
                matrix[i][j],matrix[j][i] = matrix[j][i], matrix[i][j]
        for row in matrix:
            row.reverse()
        