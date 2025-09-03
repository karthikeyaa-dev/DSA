class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sum_min = 0
        # Add every alternate element starting from index 0
        for i in range(0, len(nums), 2):
            sum_min += nums[i]
        return sum_min