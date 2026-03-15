# Problem link : https://leetcode.com/problems/next-permutation/description

# Problem Explanation:
# The task is to rearrange the given list of numbers into the lexicographically next greater permutation of numbers.
# If such an arrangement is not possible, it must rearrange it as the lowest possible order (sorted in ascending order).

# Pattern Used:
# This problem uses the "Two Pointers" pattern to find the next permutation efficiently.

# Time Complexity:
# O(n) - We traverse the array multiple times, but each traversal is linear.
# Space Complexity:
# O(1) - The solution modifies the array in-place without using extra space.

from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # If the array has only one element, no permutation is possible.
        if len(nums) == 1:
            return nums
        
        # Step 1: Find the first index from the end where nums[first_lower_index] < nums[first_lower_index + 1].
        first_lower_index = len(nums) - 2
        next_to_first_lower_index = len(nums) - 1

        while first_lower_index >= 0 and nums[first_lower_index] >= nums[next_to_first_lower_index]:
            first_lower_index -= 1
            next_to_first_lower_index -= 1
        
        # Step 2: If no such index is found, the array is in descending order.
        # Reverse the array to get the smallest permutation.
        if first_lower_index == -1:
            nums[:] = reversed(nums)
            return 
        
        # Step 3: Find the smallest number greater than nums[first_lower_index] to the right of it.
        index = first_lower_index + 1
        while index < len(nums) and nums[first_lower_index] < nums[index]:
            index += 1
        
        # Step 4: Swap nums[first_lower_index] with the found number.
        nums[first_lower_index], nums[index - 1] = nums[index - 1], nums[first_lower_index]

        # Step 5: Reverse the subarray to the right of first_lower_index to get the next permutation.
        nums[first_lower_index + 1:] = reversed(nums[first_lower_index + 1:])


# Think of a pyramid structur from right to left , rising then focus on first drop