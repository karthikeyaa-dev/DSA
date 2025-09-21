class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        while columnNumber > 0:
            columnNumber -= 1  # Adjust to 0-indexed
            result = chr(columnNumber % 26 + ord('A')) + result
            columnNumber //= 26
        return result
