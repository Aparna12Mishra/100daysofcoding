import heapq

class Graph:
    def __init__(self, n, edges):
        self.v = [[] for _ in range(101)]
        for edge in edges:
            self.v[edge[0]].append((edge[1], edge[2]))

    def addEdge(self, edge):
        self.v[edge[0]].append((edge[1], edge[2]))

    def shortestPath(self, node1, node2):
        dist = [float('inf')] * 101
        dist[node1] = 0
        pq = [(dist[node1], node1)]

        while pq:
            val, node = heapq.heappop(pq)

            for x, wt in self.v[node]:
                if dist[x] > dist[node] + wt:
                    dist[x] = dist[node] + wt
                    heapq.heappush(pq, (dist[x], x))

        return dist[node2] if dist[node2] != float('inf') else -1