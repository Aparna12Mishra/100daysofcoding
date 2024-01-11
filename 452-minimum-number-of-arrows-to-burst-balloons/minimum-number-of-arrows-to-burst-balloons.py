class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[0], x[1]))
        intervals = []
        for point in points:
            if (len(intervals) == 0):
                heapq.heappush(intervals, [-point[1], -point[0]])
            else:
                leftmost = intervals[0]
                start = -leftmost[1]
                end = -leftmost[0]
                if (point[0] <= start and point[1] >= start):
                    new_interval = [-min(point[1], end), -max(point[0], start)]
                    heapq.heappushpop(intervals, new_interval)
                elif (point[0] >= start and point[1] <= end):
                    new_interval = [-min(point[1], end), -max(point[0], start)]
                    heapq.heappushpop(intervals, new_interval)
                elif (point[0] <= end and point[1] >= end):
                    new_interval = [-min(point[1], end), -max(point[0], start)]
                    heapq.heappushpop(intervals, new_interval)
                else:
                    heapq.heappush(intervals, [-point[1], -point[0]])
        return len(intervals)     