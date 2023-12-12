class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        while i < len(s) and s[i].isspace():
            i += 1

        if i < len(s) and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1
        else:
            sign = 1

        result = 0
        max_int = 2**31 - 1
        min_int = -2**31

        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            if result > (max_int - digit) // 10:
                return max_int if sign == 1 else min_int
            result = result * 10 + digit
            i += 1

        return sign * result
        