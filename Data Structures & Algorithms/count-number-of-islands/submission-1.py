class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #Edge case and input validation
        if not grid:
            return 0

        #Variables
        islands = 0

        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            directions = [[0,1], [0, -1], [1,0], [-1,0]]
            while q:
                row, col = q.popleft()
                if (row,col) not in visited:
                    visited.add((row, col))
                #Add the neighbours
                for dr, dc in directions:
                    newr = row + dr
                    newc = col + dc
                    if (newr in range(rows) and 
                    newc in range(cols) and
                    grid[newr][newc] == "1" and 
                    (newr, newc) not in visited):
                        q.append((newr, newc))
                        visited.add((newr, newc))

                
        
        #bfs gives you all the connected components
        #Go through each cell
        rows, cols = len(grid), len(grid[0])
        visited = set() #Marking islands as visited
        #Go through each single position in the grid.
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r, c)
                    islands+=1 #Update the islands once you get a one and then you do a bfs to find all the other connected ones
                    
        return islands

                


        

        