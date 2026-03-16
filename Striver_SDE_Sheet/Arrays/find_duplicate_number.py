# Problem link : https://leetcode.com/problems/find-the-duplicate-number/description

# My Solution

# Intuituion:
# - The problem can be solved using the concept of cycle detection in a linked list.
# - We can treat the array as a linked list where the value at each index points to the next index.
# - Since there is a duplicate number, it creates a cycle in the linked list. Think of the duplicate number as a node which is being pointed to by multiple indices, creating a loop.
# - We can use Floyd's Tortoise and Hare algorithm to detect the cycle and find the duplicate number.
# - Since the numbers are in range from 1 to n, it means we can start from index 0 and no node is pointing back to index 0, so we can safely use index 0 as the starting point for our cycle detection.
from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Using Floyd's Tortoise and Hare (Cycle Detection) algorithm
        # Step 1: Initialize slow and fast pointers
        slow = 0
        fast = 0

        # Step 2: Detect the cycle
        while True:
            slow = nums[slow]  # Move slow pointer by 1 step
            fast = nums[nums[fast]]  # Move fast pointer by 2 steps
            if slow == fast:  # Cycle detected
                break

        # Step 3: Find the entrance to the cycle (duplicate number)
        slow = 0  # Reset slow pointer to the start
        while slow != fast:
            slow = nums[slow]  # Move both pointers by 1 step
            fast = nums[fast]
        
        return slow  # The duplicate number

# Time Complexity: O(n)
# - The slow and fast pointers traverse the array, and the total number of steps is proportional to the size of the array.

# Space Complexity: O(1)
# - The algorithm uses constant extra space.
