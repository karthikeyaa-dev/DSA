def combinationSum(candidates, target):
    result = []

    def backtrack(index, current, total):
        if total == target:
            result.append(current.copy())
            return
        if total > target or index == len(candidates):
            return

        # Pick current number
        current.append(candidates[index])
        backtrack(index, current, total + candidates[index])

        # Backtrack
        current.pop()

        # Skip current number
        backtrack(index + 1, current, total)

    backtrack(0, [], 0)
    return result
