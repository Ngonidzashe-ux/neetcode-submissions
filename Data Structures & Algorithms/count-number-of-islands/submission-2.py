
"""
Understand:
1. Matrix DFS

Plan:
1. Visit each cell
2. If cell is land and has not been visited, then, increment the number of islands and do a DFS to find the cells part of the same island
3. Otherwise skip it


DFS:
4. Take in the r, c
5. Base case: if r,c is visited or is water or is out of range, then we return
6. Otherwise, we add it to the visited set and visit the neighbours

"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        islands = 0
        def dfs(r, c):
            if (r, c) in visited or r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == "0":
                return
            visited.add((r,c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
                    islands+=1
        return islands

                
        