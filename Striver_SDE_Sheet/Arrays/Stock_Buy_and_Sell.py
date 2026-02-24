# Problem link : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

# My Solution
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0

        if len(prices):
            base_day_stock = prices[0]

            # Sliding window explanation:
            # The solution uses a sliding window approach where `base_day_stock` acts as the left pointer
            # (minimum price seen so far) and `current_day` iterates through the array as the right pointer.
            # The difference between the current price and the minimum price is calculated to find the maximum profit.
            # If a new minimum price is encountered, the left pointer is updated.

            # Time Complexity:
            # The solution iterates through the `prices` array once, making the time complexity O(n),
            # where n is the length of the `prices` array.

            # Space Complexity:
            # The solution uses only a constant amount of extra space (variables `max_profit` and `base_day_stock`),
            # making the space complexity O(1).

            for current_day in range(1, len(prices)):
                if prices[current_day] > base_day_stock :
                    max_profit = max(max_profit, prices[current_day] - base_day_stock)
                else:
                    base_day_stock = prices[current_day]
            
            return max_profit



