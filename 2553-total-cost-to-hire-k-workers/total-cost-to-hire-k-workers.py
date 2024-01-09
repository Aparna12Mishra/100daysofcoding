from collections import deque
from heapq import *
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:

        middle = deque()
        left = [float("inf")]
        right = [float("inf")]
        
        for i, cost in enumerate(costs):
            if i < candidates: 
                heappush(left, cost)
            elif i >= len(costs) - candidates:
                heappush(right, cost)
            else:
                middle.append(cost)


        total_cost = 0
        for _ in range(k):
            if left[0] <= right[0]:
                total_cost += heappop(left)
                middle and heappush(left, middle.popleft())
            else:
                total_cost += heappop(right)
                middle and heappush(right, middle.pop())

        return total_cost

            

            

