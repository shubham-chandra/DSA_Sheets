# Problem link : https://leetcode.com/problems/merge-intervals/description/

# My Solution

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Step 1: Sort the intervals based on the start time
        # Sorting ensures that intervals are processed in order of their start times
        sorted_intervals = sorted(intervals, key=lambda x: x[0])

        ans = []  # This will store the merged intervals
        for start, end in sorted_intervals:
            # If the result list is empty, add the first interval
            if len(ans) == 0:
                ans.append([start, end])
            # If the current interval overlaps with the last interval in the result
            elif ans[-1][1] >= start:
                # Merge the intervals by updating the end time to the maximum end time
                ans[-1][1] = max(end, ans[-1][1])
                # Update the start time to the minimum start time (optional, as intervals are sorted)
                ans[-1][0] = min(ans[-1][0], start)
            else:
                # If no overlap, add the current interval to the result
                ans.append([start, end])

        # Return the merged intervals
        return ans


