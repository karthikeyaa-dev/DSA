class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_sorted = sorted(s)
        t_sorted = sorted(t)
        for i in range(len(s)):
            if s_sorted[i] != t_sorted[i]:
                return t_sorted[i]
        return t_sorted[-1]