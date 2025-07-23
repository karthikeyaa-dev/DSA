def findMaxLength(nums):
    # Replace 0 with -1 to convert the problem to finding the longest subarray with sum 0
    prefix_sum = 0
    max_length = 0
    seen = {0: -1}  # maps prefix_sum to first index where it was seen

    for i, num in enumerate(nums):
        prefix_sum += -1 if num == 0 else 1

        if prefix_sum in seen:
            max_length = max(max_length, i - seen[prefix_sum])
        else:
            seen[prefix_sum] = i

    return max_length
