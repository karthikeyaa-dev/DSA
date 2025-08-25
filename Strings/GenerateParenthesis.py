class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(s, open_count, close_count):
            # If the current string s is of length 2*n, we have a valid combination
            if len(s) == 2 * n:
                result.append(s)
                return
            
            # If we can still add an open parenthesis, add it and recurse
            if open_count < n:
                backtrack(s + '(', open_count + 1, close_count)
            
            # If we can add a close parenthesis, add it and recurse
            if close_count < open_count:
                backtrack(s + ')', open_count, close_count + 1)
        
        backtrack('', 0, 0)
        return result
    