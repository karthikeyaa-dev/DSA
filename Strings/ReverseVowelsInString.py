class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')  # Set for O(1) lookup
        s = list(s)  # Convert string to list for in-place modifications
        left, right = 0, len(s) - 1

        while left < right:
            # Move left pointer until it points to a vowel
            while left < right and s[left] not in vowels:
                left += 1
            # Move right pointer until it points to a vowel
            while left < right and s[right] not in vowels:
                right -= 1
            # Swap the vowels
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return ''.join(s)