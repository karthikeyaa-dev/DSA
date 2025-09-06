class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # Normalize paragraph: lowercase + replace punctuation with spaces
        paragraph = re.sub(r'[^\w]', ' ', paragraph).lower()
        
        # Split into words
        words = paragraph.split()
        
        # Convert banned list to a set for faster lookup
        banned_set = set(banned)
        
        # Count frequencies excluding banned words
        word_counts = Counter(word for word in words if word not in banned_set)
        
        # Return the most common non-banned word
        return word_counts.most_common(1)[0][0]