"""
Understand Multi Source Sequentially:
- Fill each land cell with distance to its nearest treasure chest
- We can invert this and rather start from each treasure chest, sequentially to the landfill
- So we come up with a visit and q set for the specific treasure chest so we have to reinitialize these at the start of each BFS
- In the BFS, we add the starting treasure point to q, initialise dist = 0
- Then while q is not empty, we explore the current level and to ensure that we use a for loop
- Then we dequeue the node, we update the grid position with the min of the current position and the dist
- Then for each neighbouring node that is not obstacle or treasure chest, then enqueue and add it to the visit set


Understand Multi Source Simultaneously
- 
"""

#SINGLE BFS
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        INF = 2147483647

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def BFS(r, c):
            dist = 0
            visited = set()
            q = collections.deque()
            q.append((r, c))
            visited.add((r, c))
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    grid[r][c] = min(grid[r][c], dist)
                    for dr, dc in directions:
                        newr, newc = r + dr, c + dc
                        if (newr, newc) not in visited and 0 <= newr < rows and 0 <= newc < cols and grid[newr][newc] != -1 and  grid[newr][newc] != 0:
                            q.append((newr, newc))
                            visited.add((newr, newc))
                dist+=1



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    BFS(r, c)
 