class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        islands = 0
        rows = len(grid)
        cols = len(grid[0])
        visit = set()

        def bfs(r,c):
            q = collections.deque()
            q.append((r, c))
            visit.add((r,c))
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            
            while q:
                r,c = q.popleft()
                for x, y in directions:
                    nr = int(r) + x #neighbour row
                    nc = int(c)+ y
            
                    if nr in range(rows) and nc in range(cols) and (nr,nc) not in visit and   grid[nr][nc] =="1":
                        q.append((nr,nc))
                        visit.add((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c ) not in visit:
                    bfs(r,c)
                    islands+=1
        
        return islands