class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, path, total):
            # Base case: target met
            if total == target:
                result.append(path[:])
                return
            # Base case: target exceeded
            if total > target:
                return

            # Try each candidate starting from current index
            for i in range(start, len(candidates)):
                path.append(candidates[i])  # choose
                backtrack(i, path, total + candidates[i])  # allow reuse
                path.pop()  # backtrack

        backtrack(0, [], 0)
        return result   