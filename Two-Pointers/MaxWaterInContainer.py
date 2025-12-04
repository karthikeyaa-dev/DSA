def MaxWaterInContainer(height: list) -> int:
    max_area = 0
    l = len(height)
    left, right = 0, l - 1

    while left < right:
        max_area = max(max_area, min(height[left], height[right]) * (right - left))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area


n = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(MaxWaterInContainer(n))
