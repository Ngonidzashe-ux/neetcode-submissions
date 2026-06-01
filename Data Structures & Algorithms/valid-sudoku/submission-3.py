"""
Understand:
- Need to check for duplicates in 3 things:
- Rows:
- We have 9 rows so need 9 sets to check for duplicates and these can be put in a Rows dictionary
- Same with the cols and the 9 subboxes
- To determine the subbox, we do the following:
- Assume we hav a 3 * 3 matrix and therefore 0-2 rows and cols indices
- Integer division of the r,c of a cell gives us the r, c of their subbox
- We use a tuple of the subbox cordinates to identify them in the dictionary
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])
        row = collections.defaultdict(set)
        col = collections.defaultdict(set)
        box = collections.defaultdict(set)

    
        for r in range(ROWS):
            for c in range(COLS):
                digit = board[r][c]
                if (digit != "."):
                    if ((digit in row[r]) or 
                        (digit in col[c]) or
                        (digit in box[(r//3, c//3)])
                        ):
                        return False
                    else:
                        row[r].add(digit)
                        col[c].add(digit)
                        box[(r//3, c//3)].add(digit)
        return True


