class Solution:
    def eraseOverlapIntervals(self, points: List[List[int]]) -> int:
        ans = 0
        arrow = -math.inf

        for point in sorted(points, key = lambda x:x[1]):
            if(point[0] >= arrow):
                arrow = point[1]
            else:
                ans+=1

        return ans   