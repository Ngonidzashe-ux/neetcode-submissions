"""
Understand:
- If a fresh fruit is adjacent to a rotten fruit, then it gets rotten
- Minimum number of minutes = shortest time to rot all the fruits
- I am thinking of using multi source bfs and start from all the rotten fruits and rot each adjacent fresh fruit as we go
- Then at the end, traverse through the grid to find any fresh fruits and return -1 if any

Plan:
- Extract grid dimensions
- Initialise visited set and a q, directions and minute variables
- Go through the grid and add all the rotten oranges to a q and visited set i.e. grid[r][c] = 2
- While q is non empty
- We go through the q level by level using a for loop
- We pop the element at the front, and we rot it if not rotten
- Then we take the neighbours, if they are fresh, we add them to the q and visited
- Then we increment the minute variable after that level
- 
"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        q = collections.deque()
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        minute = -1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    visited.add((r, c))
                    q.append((r, c))
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if grid[r][c] == 1:
                    grid[r][c] = 2
                for dr, dc in directions:
                    newr, newc = r + dr, c + dc
                    if ((newr, newc) not in visited and 
                        0 <= newr < ROWS and 
                        0 <= newc < COLS and 
                        grid[newr][newc] == 1):
                        q.append((newr, newc))
                        visited.add((newr, newc))
            minute += 1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
        return max(minute, 0)
        