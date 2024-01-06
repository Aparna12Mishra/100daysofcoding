class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans = sum(nums[:k])
        window = ans
        for i in range(1,len(nums)-k+1):            
            window = window - nums[i-1] + nums[i+k-1]
            ans = max(window, ans)
        return ans/k