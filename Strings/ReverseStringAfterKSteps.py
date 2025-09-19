class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        arr = list(s)
        for i in range(0, len(s), 2 * k):
            # Reverse the first k characters for every 2k segment
            arr[i:i+k] = reversed(arr[i:i+k])
        return ''.join(arr)