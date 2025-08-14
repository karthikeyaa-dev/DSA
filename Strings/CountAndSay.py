class Solution(object):
    def countAndSay(self, n):
        if n == 1:
            return "1"

        result = "1"
        for _ in range(2, n + 1):
            current = ""
            i = 0
            while i < len(result):
                count = 1
                # Count consecutive digits
                while i + 1 < len(result) and result[i] == result[i + 1]:
                    i += 1
                    count += 1
                # Append "count + digit" to current result
                current += str(count) + result[i]
                i += 1
            result = current

        return result

        