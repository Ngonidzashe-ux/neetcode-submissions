class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            if (r < 0 or r >= rows or c < 0 or c >= cols
            or board[r][c] != 'O'):
                return
            board[r][c] = 'T'
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)



        #Change the unsurrounded to T, this means that all O's that are connected
        #to the O's on the boarder and therefore we want to do dfs search from the O's on the border
        for r in range(rows):
            for c in range(cols):
                if (r == rows - 1 or r == 0 or c == 0 or c == cols - 1) and board[r][c] == 'O':
                    dfs(r, c)

        #Change the surrounded from O to X
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
        

        #Change the temp variables back to 'O'
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'T':
                    board[r][c] = 'O'

        