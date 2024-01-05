class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s = list(s)
        length = len(s)

        c = 0
        for i in t:
            try:
                if i == s[c]:
                    c += 1
            except:
                continue
        if c == length:
            return True
        return False
                