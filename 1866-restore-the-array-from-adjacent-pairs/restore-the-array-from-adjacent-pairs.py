class Solution:
    def restoreArray(self, adjacentPairs):
        n = len(adjacentPairs) + 1

        # Build the graph
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for pair in adjacentPairs:
            graph[pair[0]].append(pair[1])
            graph[pair[1]].append(pair[0])
            indegree[pair[0]] += 1
            indegree[pair[1]] += 1

        # Find the start/end node
        start = None
        for node, deg in indegree.items():
            if deg == 1:
                start = node
                break

        # Traverse the graph
        curr, prev = start, float('-inf')
        nums = []
        while len(nums) < n:
            nums.append(curr)
            for next_node in graph[curr]:
                if next_node != prev:
                    prev, curr = curr, next_node
                    break

        return nums