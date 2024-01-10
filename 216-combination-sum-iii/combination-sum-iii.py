class Solution:
    @lru_cache
    def combinationSum3(self, k: int, n: int, m: int = 1) -> List[List[int]]:
        if n < k or n > min(k * 9, 45):
            return []
        if k == 1 and n >= m:
            return [[n]]
        ret = []
        for i in range(m, 10):
            for ans in self.combinationSum3(k - 1, n - i, i + 1):
                ret.append([i] + ans)
        return ret