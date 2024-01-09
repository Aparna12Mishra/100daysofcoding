from collections import deque

class Solution:

    def orangesRotting(self, grid: List[List[int]]) -> int:
        n_rows, n_cols = len(grid), len(grid[0])
        q, n_fresh, n_mins = deque(), 0, 0

        for r in range(n_rows):
            for c in range(n_cols):
                if grid[r][c] == 1:
                    n_fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while n_fresh > 0 and q:
            for _ in range(len(q)): 
                r, c = q.popleft()

                for rd, cd in dirs:
                    ri, ci = r + rd, c + cd
                    if 0 <= ri < n_rows and 0 <= ci < n_cols and grid[ri][ci] == 1:
                        grid[ri][ci] = 2
                        n_fresh -= 1
                        q.append((ri, ci))
            n_mins += 1

        return n_mins if n_fresh == 0 else -1