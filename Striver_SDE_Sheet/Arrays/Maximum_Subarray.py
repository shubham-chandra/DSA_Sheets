# Problem link : https://leetcode.com/problems/maximum-subarray/description

# My Solution
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # This solution uses Kadane's Algorithm, which is a dynamic programming approach
        # to find the maximum sum of a contiguous subarray. It works by maintaining two variables:
        # 1. max_so_far: Tracks the maximum sum of subarray ending at the current position.
        # 2. final_max: Tracks the overall maximum sum encountered so far.
        
        final_max = nums[0]
        max_so_far = nums[0]

        for i in range(1, len(nums)):
            max_so_far = max(max_so_far + nums[i], nums[i])
            final_max = max(max_so_far, final_max)
        
        return final_max

