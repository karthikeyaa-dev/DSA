from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Start from the end of nums1 and nums2
        p1 = m - 1  # Pointer to the last actual element in nums1
        p2 = n - 1  # Pointer to the last element in nums2
        p = m + n - 1  # Pointer to the end of nums1

        # While both arrays have elements to compare
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # If any elements left in nums2 (nums1 already in place if p1 >= 0)
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
        