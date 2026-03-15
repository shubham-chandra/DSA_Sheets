# Problem link : https://leetcode.com/problems/rotate-image

# My Solution

# This problem uses the "Matrix Manipulation" pattern.
# The goal is to rotate the given n x n 2D matrix 90 degrees clockwise in-place.
# The rotation can be achieved in two steps:
# 1. Transpose the matrix along its diagonal.
# 2. Reverse each row (or equivalently flip the matrix along its middle column).

def flip_along_diagonal(matrix):
    """
    Transpose the matrix along its diagonal.
    This means converting rows to columns and columns to rows.
    """
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if i <= j:  # Only swap elements above the diagonal (including diagonal).
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

def flip_along_middle_column(matrix):
    """
    Reverse each row of the matrix (flip along the middle column).
    This completes the 90-degree clockwise rotation.
    """
    n = len(matrix)
    first_col = 0
    last_col = n - 1

    while first_col < last_col:
        for row in range(n):
            matrix[row][first_col], matrix[row][last_col] = matrix[row][last_col], matrix[row][first_col]
        first_col += 1
        last_col -= 1

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Rotate the matrix 90 degrees clockwise in-place.

        Steps:
        1. Transpose the matrix along its diagonal.
        2. Reverse each row (flip along the middle column).

        Time Complexity:
        - Transposing the matrix takes O(n^2) time, where n is the number of rows/columns.
        - Reversing each row also takes O(n^2) time.
        - Overall time complexity: O(n^2).

        Space Complexity:
        - The solution is in-place, so the space complexity is O(1).
        """
        flip_along_diagonal(matrix)
        flip_along_middle_column(matrix)
