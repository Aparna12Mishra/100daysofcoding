class Solution:
    def countSetBits(self, n):
        count = 0
        while n > 0:
            n = n & (n - 1)
            count += 1
        return count

    def sortByBits(self, arr):
        bits = []

        for x in arr:
            count = self.countSetBits(x)
            bits.append((count, x))

        bits.sort()
        ans = [x for _, x in bits]
        return ans
