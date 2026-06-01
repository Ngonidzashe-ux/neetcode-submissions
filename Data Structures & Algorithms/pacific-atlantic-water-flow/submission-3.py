"""
Plan:
- Initialise atl and pac with the boarder cells
- Then start  at the bottom row and top row, for each cell, traverse using BFS to see which ones it can reach
- Then do the same for left and right
- Then check the two ocean sets and return whoever is in both
"""

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atl, pac = set(), set()
        ROWS, COLS = len(heights), len(heights[0])

        def dfs(r, c, prev, ocean):
            if ocean == "a":
                if ((r, c) in atl or not (0 <= r < ROWS) or not (0 <= c < COLS) or prev > heights[r][c]):
                    return
                atl.add((r, c))
                dfs(r + 1, c, heights[r][c], ocean)
                dfs(r - 1, c, heights[r][c], ocean)
                dfs(r, c + 1, heights[r][c],ocean )
                dfs(r, c - 1, heights[r][c],ocean )
            else:
                if ((r, c) in pac or not (0 <= r < ROWS) or not (0 <= c < COLS) or prev > heights[r][c]):
                    return
                pac.add((r, c))
                dfs(r + 1, c, heights[r][c], ocean)
                dfs(r - 1, c, heights[r][c], ocean)
                dfs(r, c + 1, heights[r][c], ocean)
                dfs(r, c - 1, heights[r][c], ocean)

        #Start with bottom and top rows
        for c in range(COLS):
            dfs(0, c, 0, "p")
            dfs(ROWS - 1, c, 0, "a")
        
        for r in range(ROWS):
            dfs(r, 0, 0, "p")
            dfs(r, COLS - 1, 0, "a")

        res = []
        for cell in atl:
            if cell in pac:
                res.append(list(cell))
        return res
