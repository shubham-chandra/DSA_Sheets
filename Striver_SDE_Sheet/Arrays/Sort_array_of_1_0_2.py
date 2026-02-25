# Problem link : https://leetcode.com/problems/sort-colors/submissions

# My Solution
from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # This problem is solved using the Dutch National Flag algorithm.
        # The idea is to maintain three pointers:
        # 1. 'low' for the boundary of 0s
        # 2. 'mid' for the current element being processed
        # 3. 'high' for the boundary of 2s
        # The algorithm ensures that all elements before 'low' are 0s,
        # all elements between 'low' and 'mid' are 1s, and all elements after 'high' are 2s.

        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                # Swap the current element with the element at 'low'
                # and move both 'low' and 'mid' pointers forward. 
                # We will get 1 from the low side so we can move mid pointer also 1 step forward.
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                # If the current element is 1, just move the 'mid' pointer forward.
                mid += 1
            else:  # nums[mid] == 2
                # Swap the current element with the element at 'high'
                # and move the 'high' pointer backward.
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1


