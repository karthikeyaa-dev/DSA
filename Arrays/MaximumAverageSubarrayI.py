from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Compute initial window sum
        window_sum = sum(nums[:k])
        max_sum = window_sum

        # Slide the window across the array
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, window_sum)

        # Return the average
        return max_sum / k
            