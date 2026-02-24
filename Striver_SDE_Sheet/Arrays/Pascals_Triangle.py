# Problem link : https://leetcode.com/problems/pascals-triangle/description/

# My Solution

# Pattern used:
# Pascal's Triangle is constructed such that each element is the sum of the two elements directly above it.
# The first and last elements of each row are always 1.

# Time Complexity:
# The outer loop runs `numRows` times, and the inner loop iterates over the length of the current row.
# This results in a total of O(numRows^2) operations.

# Space Complexity:
# The space used is proportional to the size of the result, which is O(numRows^2).

from typing import List
class Solution:


    def generate_next_row(self,input_row):
        output_row = [1] * (len(input_row) + 1)

        if len(input_row) >= 2:
            for i in range(1,len(input_row)):
                output_row[i] = input_row[i] + input_row[i-1]
        
        return output_row

    def generate(self, numRows: int) -> List[List[int]]:

        result_list = [0] * numRows

        base_row = []

        for i in range(numRows):
            result_list[i] = self.generate_next_row(base_row)
            base_row = result_list[i]
        
        return result_list



