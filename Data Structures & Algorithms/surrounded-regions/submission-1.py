""""
Understand: Find surrounded regions and capture them
The other way is that find the unsurrounded regions and mark them and only capture the rest
Input: Given a board, return None, modify inplace
Constraints: Cells are 4 way directionally connected
Edge cases: board = [[]], board is only x or something else
Assumptions. We are gonna get X and 0s

"""

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return 
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        directions = []

        def dfs(r, c):
            if (not (0 <= r < ROWS) or
                not (0 <= c < COLS) or
                board[r][c] != "O" or
                (r, c) in visited
            ):
                return
            board[r][c] = "T"
            visited.add((r, c))
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for r in range(ROWS):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][COLS - 1] == "O":
                dfs(r, COLS - 1)
        
        for c in range(COLS):
            if board[0][c] == "O":
                dfs(0, c)
            if board[ROWS - 1][c] == "O":
                dfs(ROWS - 1, c)


        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
        
        