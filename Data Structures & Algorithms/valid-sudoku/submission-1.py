class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #I need to have a hashset for each of the 9 rows
        #Another hashset for one of the columns and the squares
        #We are gonna store all the row hashset in the rows hashset and the similar thing with everything else
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        #Then we iterate through the board, through each element
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r//3, c//3)]):
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        return True


        

        
            
        