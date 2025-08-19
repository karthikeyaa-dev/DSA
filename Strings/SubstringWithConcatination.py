from collections import Counter
class Solution(object):
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        word_len = len(words[0])
        num_words = len(words)
        concat_len = word_len * num_words
        word_count = Counter(words)
        result = []

        for i in range(word_len):
            left = i
            right = i
            seen = Counter()

            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len

                if word in word_count:
                    seen[word] += 1

                    # If word appears more times than expected, move left window
                    while seen[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        left += word_len

                    # If window matches size of concatenated words, store result
                    if right - left == concat_len:
                        result.append(left)
                else:
                    # Reset if the word is not in words
                    seen.clear()
                    left = right

        return result

        