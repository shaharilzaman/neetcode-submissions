from typing import List
import collections

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        
        def bfs(r, c):
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))
            while q:
                row, col = q.pop()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    r , c = row + dr, col + dc
                    if (r in range(rows)
                        and c in range(cols)
                        and grid[r][c] == "1"
                        and (r, c) not in visited):
                        visited.add((r,c))
                        q.append((r,c))
        output = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]== '1' and (r,c) not in visited:
                    bfs(r,c)
                    output+= 1
        return output