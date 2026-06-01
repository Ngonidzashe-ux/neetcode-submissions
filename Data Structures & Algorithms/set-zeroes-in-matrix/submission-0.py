class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        #This is the extra variable that we need
        #This is gonna tell us if the first row has to be zeroed or not
        #Set it to False first
        rowZero = False

        #iterate over every row and column which is basically iterating through every cell
        for r in range(ROWS):
            for c in range(COLS):
                #If we find an entry thats 0, we are going to go to the top row, and set the
                # the column corresponding to the entry to 0 which indicates that we need to zero the column at some point.
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    #If the row is not the first one, then go to the corresponding row and look for the first column of that row and 
                    #set that to 0 to indicate that the specific row should be set to 0 at some point
                    if r > 0:
                        matrix[r][0] = 0
                    #If its the first row, just update rowZero to be True
                    else:
                        rowZero = True
        #After all that,we are gonna iterate each position again and try to update the columns and rows that need updates.
        #Note though that we are gonna skip the first column and the first row.
        for r in range(1, ROWS):
            for c in range(1, COLS):
                #For the current cell that we are in, if the column needs to be zeroed or the row need to be zeroed, then zero the current position matrix[r][c]
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
#If the first column is 0, then we can set all the values in the first column to zero.
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
#If the first row is zero, which is indicated by our variable rowZero, then we have to zero the whole first row
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0
