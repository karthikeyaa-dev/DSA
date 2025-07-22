def two_sum_unique_pairs(nums, target):
    seen = set()
    output = {
        tuple(sorted((num, target - num)))
        for num in nums
        if (target - num) in seen or not seen.add(num)
    }
    return [list(pair) for pair in output]
