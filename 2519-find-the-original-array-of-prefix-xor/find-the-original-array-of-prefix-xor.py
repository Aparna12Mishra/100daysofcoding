class Solution:
    def findArray(self, pref):
        n = len(pref)
        ans = [0] * n
        ans[0] = pref[0]
        
        for i in range(1, n):
            ans[i] = pref[i - 1] ^ pref[i]
        
        return ans
  