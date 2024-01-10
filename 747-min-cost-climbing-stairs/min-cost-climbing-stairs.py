class Solution:
    def minCostClimbingStairs(self, c: List[int]) -> int:
        n = len(c)
        dp = [0]*(n+1)
        dp[n] = 0
        dp[n-1] = c[-1]
        for i in range(len(c)-2,-1,-1):
            dp[i] = min(c[i] + dp[i+1],c[i] + dp[i+2])
        return min(dp[0],dp[1])



        