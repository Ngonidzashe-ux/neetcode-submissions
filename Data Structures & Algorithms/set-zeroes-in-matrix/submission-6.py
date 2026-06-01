"""
Understand:
- If an element is 0, set the whole row and col to 0
- We cant change the rows and cols based on each individual value as this will erase some info
- Use the top row and left col to indicate the rows/cols to be zeroed
- The first element represents the cols, so have a variable that stores the rowZero info
- Then after, we go throught the left col and first row and we zero the other parts
- Then check the first cell to see if we zero the left col
- Check row Zero to see if we zero the top row
"""

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    if r == 0:
                        rowZero = True
                    else:
                        matrix[r][0] = 0
                    matrix[0][c] = 0
        
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[r][0] == 0:
                    matrix[r][c] = 0
                if matrix[0][c] == 0:
                    matrix[r][c] = 0
        
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0



        
        