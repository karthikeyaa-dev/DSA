class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))  # Remove duplicates
        nums.sort(reverse=True)  # Sort in descending order
        if len(nums) >= 3:
            return nums[2]  # Return the third distinct maximum
        else:
            return nums[0]  # Return the maximum if fewer than 3 distinct elements