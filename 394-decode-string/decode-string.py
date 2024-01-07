class Solution:
    def decodeString(self, s: str) -> str:
        cur_num = 0
        cur_str = ""
        stack = []

        for char in s:
            if char.isdigit():
                cur_num = cur_num * 10 + int(char)
            elif char == "[":
                stack.append((cur_str, cur_num))
                cur_num = 0
                cur_str = ""
            elif char == "]":
                prev_str, cur_num = stack.pop()
                cur_str = prev_str + cur_str * cur_num
                cur_num = 0
            else:
                cur_str += char
        return cur_str