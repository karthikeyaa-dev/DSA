from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        
        # Start from the last digit and move backward
        for i in range(n - 1, -1, -1):
            # If current digit is less than 9, just add 1 and return
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # If digit is 9, it becomes 0 and we carry 1 to the next digit
            digits[i] = 0
        
        # If all digits are 9, we get here after loop and need to add 1 at the front
        return [1] + digits