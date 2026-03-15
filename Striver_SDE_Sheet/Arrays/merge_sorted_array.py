# Problem link : https://leetcode.com/problems/merge-sorted-array/description/
# My Solution

from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # Initialize pointers:
        # index_to_fill points to the last position in nums1 where the merged element will be placed.
        # index_to_compare_1 points to the last valid element in nums1.
        # index_to_compare_2 points to the last element in nums2.
        index_to_fill = m + n - 1
        index_to_compare_1 = m - 1
        index_to_compare_2 = n - 1

        # Iterate while there are elements left in nums2 to merge.
        while index_to_compare_2 >= 0:
            # If nums1 has elements left to compare and the current element in nums1 is greater than the current element in nums2,
            # place the nums1 element at the index_to_fill position.
            if index_to_compare_1 >= 0 and nums1[index_to_compare_1] > nums2[index_to_compare_2]:
                nums1[index_to_fill] = nums1[index_to_compare_1]
                index_to_fill -= 1
                index_to_compare_1 -= 1
            else:
                # Otherwise, place the nums2 element at the index_to_fill position.
                nums1[index_to_fill] = nums2[index_to_compare_2]
                index_to_fill -= 1
                index_to_compare_2 -= 1

        # Explanation of the pattern:
        # This approach uses the two-pointer technique, starting from the end of both arrays.
        # By filling nums1 from the back, we avoid overwriting elements in nums1 that are yet to be compared.
        # The algorithm ensures that nums1 is modified in-place and remains sorted after merging.

        # Time Complexity:
        # The algorithm iterates through nums2 and possibly nums1 once, so the time complexity is O(m + n),
        # where m is the number of initial elements in nums1 and n is the number of elements in nums2.

        # Space Complexity:
        # The algorithm uses constant extra space (only pointers), so the space complexity is O(1).


