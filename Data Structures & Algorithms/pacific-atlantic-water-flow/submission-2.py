class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        #Determine the cells that can reach pacific and atlantic seperately and then check for the cells found in both
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()
        res = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(r, c, visit, prevheight):
            if not (0 <= r < rows and 
                0 <= c < cols and
                heights[r][c] >= prevheight and
                (r,c) not in visit):
                return
            visit.add((r,c))
            for dr, dc in directions:
                newr = r + dr
                newc = c + dc
                dfs(newr, newc, visit, heights[r][c])


        for c in range(cols):
            dfs(0, c, pac, 0)
            dfs(rows-1, c, atl, 0)
        for r in range(rows):
            dfs(r, 0, pac, 0)
            dfs(r, cols-1, atl, 0)
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res
        
        
