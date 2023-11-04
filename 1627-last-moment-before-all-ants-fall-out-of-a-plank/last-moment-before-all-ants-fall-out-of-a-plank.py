class Solution:
    def getLastMoment(self, n, left, right):
        res = 0
        for j in left:
            res = max(res, j)
        for j in right:
            res = max(res, n - j)
        return res      