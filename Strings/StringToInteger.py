class Solution(object):
    def myAtoi(self, s):
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        i = 0
        n = len(s)
        result = 0
        sign = 1

        # 1. Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        # 2. Handle sign
        if i < n and (s[i] == '-' or s[i] == '+'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        # 3. Convert digits
        while i < n and s[i].isdigit():
            digit = int(s[i])

            # 4. Check for overflow
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN

            result = result * 10 + digit
            i += 1

        return sign * result