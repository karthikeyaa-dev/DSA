class Solution(object):
    def longestValidParentheses(self, s):
        max_len = 0
        stack = [-1]  # Start with base index

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:  # char == ')'
                stack.pop()
                if not stack:
                    stack.append(i)  # New base index
                else:
                    max_len = max(max_len, i - stack[-1])

        return max_len

        