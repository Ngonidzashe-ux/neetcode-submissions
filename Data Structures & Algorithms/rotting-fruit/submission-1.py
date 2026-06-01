#1. Go through all the cells and if the cell is rotten fruit, add it to a queue
#2. Do a bfs from all the cells that are rotten and minute depens on the distance from the orginal wroteen

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()
        q = deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                    visited.add((r, c))
                if grid[r][c] == 1:
                    fresh += 1

        minutes = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = 2
                for dr, dc in directions:
                    newr, newc = r + dr, c + dc
                    if ((newr, newc) not in visited and 
                        0 <= newr < rows and 
                        0 <= newc < cols and 
                        grid[newr][newc] == 1
                        ):
                            q.append((newr, newc))
                            visited.add((newr, newc))
                            fresh -= 1

            if q:
                minutes+=1

        if fresh:
            return -1
        return minutes


        