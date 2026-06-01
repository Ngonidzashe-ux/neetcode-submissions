class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #First thing to do with Matrices, get the dimensions first
        ROWS, COLS = len(heights), len(heights[0])

        #Mantains the positions/cells that can reach the pacific and atlantic respectively
        pac, atl = set(), set()

        #Pass in visit as the parameter since we are using either of the two visit sets
        def dfs(r, c, visit, prevHeight):
            #If we have visited the cell already,
            if (
                (r, c) in visit
                or r < 0 #or go out of bounds i.e lower than the matrix
                or c < 0
                or r == ROWS #higher than the matric
                or c == COLS
                or heights[r][c] < prevHeight #If the height or the current row column position is less than the prevheight
            ):
                return
            visit.add((r, c)) #If we are not returning then, we need to add that position inside the visit
            #Then call dfs on the neighbours
            
            dfs(r + 1, c, visit, heights[r][c]) #right
            dfs(r - 1, c, visit, heights[r][c]) #left
            dfs(r, c + 1, visit, heights[r][c]) #up
            dfs(r, c - 1, visit, heights[r][c]) #down
        #Go through every single column/pos in the first row and first row is the pacific
        for c in range(COLS):
            #On each cell, we are going to run dfs and we pass in the pac visit set and the previous height which would be the cell we are coming from
            #Since for this one, we are coming from the ocean, we can give the prev height or value that is same as the cell we are doing dfs on because 
            #Then it means that we are able to move from the ocean to the cell
            dfs(0, c, pac, heights[0][c])
            #Go through every position in the last row for the atlantic ocean
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])
        #Go through the same
        for r in range(ROWS):
            #first col
            dfs(r, 0, pac, heights[r][0])
            #last col
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        res = []
        #Now we want to go through each single cell and if the position is in both pac and atl then add it to the results.append and return the results array
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res
