"""
1. Go through each cell and if its land, then we do dfs traversal
2. Dfs on a cell should return length to treasure chest, if it can't then should return and do nothing

I am not sure about the following:
1. Should i have a variable keeping track of the length to the treasure chest and return 
"""


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()
        q = collections.deque()
        INF = 2147483647


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))
        def addRoom(r, c):
            if not (0 <= r < rows and 
            0 <= c < cols and 
            (r, c) not in visited and 
            grid[r][c] == INF
            ):
                return 
            q.append((r, c))
            visited.add((r, c))
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                for dr, dc in directions:
                    addRoom(r + dr, c + dc)
            dist+=1
            

        
        