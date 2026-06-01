"""
Understand:
Given a 2d-grid of characters board and a string word, return True if the word is present
Input, str and List[List[str]] and output = true/false
Edge cases, if there is no board or word
Constraints. None

Plan:
if not word:
    return True
if not board:
    return False
ROWS, COLS = len(board), len(board[0])
def dfs(r, c, i):
    if i >= len(word):
        return True
    if (not (0 <= r < ROWS) or 
    not (0 <= c < COLS) or 
    (r, c) in visited or 
    board[r][c] != word[i]):
        return False
    
    if (dfs(r+1, c, i+1) or
     dfs(r-1, c, i+1) or 
     dfs(r, c+1, i+1) or
    dfs(r-1, c-1, i+1)):
        return True
    return False




    

for r in range(ROWS):
    for c in range(COLS):
        if board[r][c] == word[0]:
            if dfs(r, c, 0):
                return True
return False


"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True
        if not board:
            return False
        ROWS, COLS = len(board), len(board[0])
        path = set()
        def dfs(r, c, i):
            if i >= len(word):
                return True
            if (not (0 <= r < ROWS) or 
            not (0 <= c < COLS) or 
            (r, c) in path or
            board[r][c] != word[i]):
                return False

            path.add((r, c))
            if (dfs(r+1, c, i+1) or
            dfs(r-1, c, i+1) or 
            dfs(r, c+1, i+1) or
            dfs(r, c-1, i+1)):
                return True
            path.remove((r, c))
            return False

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
        return False    