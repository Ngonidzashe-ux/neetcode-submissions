class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #This is us initialising the bottom row with ones because the number
        #of unique paths to reach target is 1 for all the cells in the last row
        #because you can only move right and can't go down
        row = [1]*n

        #Since we know the bottom row is all 1s, we can start going through other rows
        #Start from bottom less 1 w
        for i in range(m-2, -1, -1):
            #create a new row that is above the old row
            newRow = [1]*n

            #Then we are gonna go through each position in the row except the right most col
            #Basically starting from the second to last position
            for j in range(n-2,-1, -1):
                #The current value of a row is a result of adding
                #the below value and the one on the right
                newRow[j] = newRow[j+1] + row[j]
            #After we do that, we update the old row
            row = newRow
        return row[0]

