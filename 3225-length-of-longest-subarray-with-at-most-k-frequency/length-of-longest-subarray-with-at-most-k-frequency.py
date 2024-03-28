class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        i = j = 0
        n = len(nums)
        ans = 1
        map = {}

        while i < n:
            map[nums[i]] = map.get(nums[i], 0) + 1
            while map[nums[i]] > k:
                map[nums[j]] -= 1
                j += 1
            ans = max(ans, i - j + 1)
            i += 1
        return ans