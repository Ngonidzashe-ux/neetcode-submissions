"""
Understand:
Return the cells that we can reach from both the pacific and the atlantic ocean
Input: heights 2d list, output: List of lists
Constraints: Water flows from a higher cell into a lower cell
Edge cases: Empty grid, same height through out, 

Match:
Like Course Schedule, we can use DFS starting from each cell bordering each ocean.
Place them into sets and then we return those cells found in both sets



Plan:
if not heights:
    return []
ROWS, COLS = len(heights), len(heights[0])
atl, pac = set(), set()

def dfs(r, c, prevHeight, visited):
    if (not (0 <= r < ROWS) or
        not (0 <= c < COLS) or
        (r, c) in visited or
         heights[r][c] > prevHeight):
         return
    visited.add((r, c))
    dfs(r + 1, c, heights[r][c], visited)
    dfs(r, c + 1, heights[r][c], visited)
    dfs(r - 1, c, heights[r][c], visited)
    dfs(r, c - 1, heights[r][c], visited)


for r in range(ROWS):
    for c in range(COLS):
        if c == 0:
            dfs(r, c, 0 pac)
        if c == COLS - 1:
            dfs(r, c, 0, atl)
        if r == 0:
            dfs(r, c, 0,  pac)
        if r == ROWS - 1:
            dfs(r, c, 0, pac)


res = []
for tuple in atl:
    if tuple in pac:
        res.add(list(tuple))
return res
"""

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        ROWS, COLS = len(heights), len(heights[0])
        atl, pac = set(), set()

        def dfs(r, c, prevHeight, visited):
            if (not (0 <= r < ROWS) or
                not (0 <= c < COLS) or
                (r, c) in visited or
                heights[r][c] < prevHeight):
                return
            visited.add((r, c))
            dfs(r + 1, c, heights[r][c], visited)
            dfs(r, c + 1, heights[r][c], visited)
            dfs(r - 1, c, heights[r][c], visited)
            dfs(r, c - 1, heights[r][c], visited)


        for r in range(ROWS):
            for c in range(COLS):
                if c == 0:
                    dfs(r, c, 0, pac)
                if c == COLS - 1:
                    dfs(r, c, 0, atl)
                if r == 0:
                    dfs(r, c, 0,  pac)
                if r == ROWS - 1:
                    dfs(r, c, 0, atl)


        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res  