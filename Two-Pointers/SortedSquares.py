nums = [-9, -6, -2, 5, 2, 4, 5]

# Two-pointer approach
left, right = 0, len(nums) - 1
res = [0] * len(nums)
i = len(nums) - 1

while left <= right:
    if abs(nums[left]) > abs(nums[right]):
        res[i] = nums[left]**2
        left += 1
    else:
        res[i] = nums[right]**2
        right -= 1
    i -= 1

print(res)
