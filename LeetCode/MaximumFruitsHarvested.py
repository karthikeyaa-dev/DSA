class Solution(object):
    def maxTotalFruits(self, fruits, startPos, k):
        n = len(fruits)
        max_total = 0
        left = 0
        total = 0

        for right in range(n):
            total += fruits[right][1]
            while left <= right:
                l_pos = fruits[left][0]
                r_pos = fruits[right][0]

                cost = min(
                    abs(startPos - l_pos) + (r_pos - l_pos),
                    abs(startPos - r_pos) + (r_pos - l_pos)
                )

                if cost <= k:
                    break

                total -= fruits[left][1]
                left += 1

            max_total = max(max_total, total)

        return max_total

