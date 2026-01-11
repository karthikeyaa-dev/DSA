from math import factorial


def getPermutation(n: int, k: int) -> str:
    nums = list(range(1, n + 1))
    k -= 1  # convert to 0-indexed
    result = []

    for i in range(n, 0, -1):
        f = factorial(i - 1)
        index = k // f
        result.append(str(nums[index]))
        nums.pop(index)
        k %= f

    return "".join(result)


# Example
print(getPermutation(3, 4))  # Output: "231"
