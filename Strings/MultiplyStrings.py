class Solution(object):
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"

        n, m = len(num1), len(num2)
        result = [0] * (n + m)

        # Reverse loop through both strings
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                p1 = i + j
                p2 = i + j + 1

                # Add to current position
                total = mul + result[p2]

                result[p2] = total % 10
                result[p1] += total // 10

        # Skip leading zeros
        result_str = ''.join(map(str, result)).lstrip('0')
        
        return result_str or "0"
            