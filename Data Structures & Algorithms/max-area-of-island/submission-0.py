"""
1. We are counting the 1's in one connected component so we dont return True or False
2. Go through each cell in the grid.
3. If the cell is 1, then we have to run dfs where we are counting the number of connected components
4. We can keep a variable that tracks the length

"""

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def dfs(r, c, visited):
            if not ((r, c) not in visited and 
                0 <= r < rows and
                 0 <= c < cols and 
                 grid[r][c] == 1
            ):
                return 0
            area = 1
            visited.add((r,c))
            for dr, dc in directions:
               area += dfs(r + dr, c + dc, visited)
            return area
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    visited = set()
                    maxArea = max(maxArea, dfs(r, c, visited))
        return maxArea
                