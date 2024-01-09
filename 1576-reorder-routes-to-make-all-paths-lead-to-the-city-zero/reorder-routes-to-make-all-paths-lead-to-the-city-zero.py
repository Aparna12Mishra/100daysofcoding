class Solution:
       def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = [ [] for i in range(0,n)]

        for item in connections:
            graph[item[0]].append( [item[1],0] )
            graph[item[1]].append( [item[0],1] )

        dq = deque()
        dq.append(0)
        visited = [0 for i in range(0,n)]
        visited[0] = 1
        res = 0
        while(len(dq)>0):
            v = dq.popleft()
            for neib,neg in graph[v]:
                if(visited[neib] == 0 ):
                    visited[neib] = 1
                    dq.append(neib);
                    if(neg): res += 1
        return n-1-res