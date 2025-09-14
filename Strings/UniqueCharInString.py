class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Count frequency of each character
        count = Counter(s)
        
        # Find the index of the first unique character
        for i, char in enumerate(s):
            if count[char] == 1:
                return i
        
        return -1