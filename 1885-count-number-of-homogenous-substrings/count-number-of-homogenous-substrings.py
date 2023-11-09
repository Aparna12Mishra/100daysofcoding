class Solution:
    def countHomogenous(self, s):
        M = 10**9 + 7
        mp = {}
        ans = 0
        mp[s[0]] = 1
        ans += 1
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                del mp[s[i - 1]]
                mp[s[i]] = 1
                ans += 1
            else:
                mp[s[i]] = mp.get(s[i], 0) + 1
                ans += mp[s[i]]
                ans %= M
        return ans
