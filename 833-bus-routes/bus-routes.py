from collections import deque, defaultdict

class Solution:
    def numBusesToDestination(self, routes, S, T):
        to_routes = defaultdict(list)
        for i in range(len(routes)):
            for j in routes[i]:
                to_routes[j].append(i)
        
        bfs = deque([(S, 0)])
        seen = {S}
        
        while bfs:
            stop, bus = bfs.popleft()
            if stop == T:
                return bus
            
            for i in to_routes[stop]:
                for j in routes[i]:
                    if j not in seen:
                        seen.add(j)
                        bfs.append((j, bus + 1))
                
                # Clear visited stops to avoid revisiting them
                routes[i] = []
        
        return -1