# problem link :https://leetcode.com/problems/set-matrix-zeroes/

# My Solution
from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Approach: Use the first row and first column as markers to indicate which rows and columns should be set to zero.
        # Pattern: Matrix manipulation with in-place marking.
        # Time Complexity: O(ROW * COL), where ROW is the number of rows and COL is the number of columns in the matrix.
        # Space Complexity: O(1), as no additional space is used apart from the input matrix.

        first_row_zero = False
        first_column_zero = False

        ROW = len(matrix)
        COL = len(matrix[0])

        # Check if the first column should be set to zero
        for i in range(ROW):
            if matrix[i][0] == 0:
                first_column_zero = True
        
        # Check if the first row should be set to zero
        for i in range(COL):
            if matrix[0][i] == 0:
                first_row_zero = True

        # Use the first row and column as markers for rows and columns to be set to zero
        for i in range(ROW):
            for j in range(COL):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Set the appropriate columns to zero based on the markers in the first row
        for col in range(1, COL):
            if matrix[0][col] == 0:
                for row in range(ROW):
                    matrix[row][col] = 0
        
        # Set the appropriate rows to zero based on the markers in the first column
        for row in range(1, ROW):
            if matrix[row][0] == 0:
                for col in range(COL):
                    matrix[row][col] = 0
        
        # Handle the first row separately if it needs to be set to zero
        if first_row_zero:
            for i in range(COL):
                matrix[0][i] = 0
        
        # Handle the first column separately if it needs to be set to zero
        if first_column_zero:
            for i in range(ROW):
                matrix[i][0] = 0