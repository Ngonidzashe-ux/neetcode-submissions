"""
Understand:
- Given a 2D grid of letters and a word, return true if the word can be found in the grid
- Input: 2D grid of letters and the word, output = true or false
- Edge cases: grid = [], grid = something but word = "", 
- Assumptions: grid has letters in caps all the time, word is in caps too
- Constraints: A cell can only be visited once when searching for the path that gives the word.

Understand: Given a 2D grid of uppercase letters and an 
uppercase word, return True if the word can be formed by 
a path of adjacent cells (up, down, left, right), using 
each cell once. Input: List[List[str]], str; Output: bool.
Edge cases: grid = [], word = "", single cell, word longer 
than grid, no valid path.”



Match:
- This is similar to combination sum, in that there is backtracking when you choose a path that is not feasible
- We can utilise the same thing here in that if the cell we are on does not work, we backtrack to find the cell that works
- This is also similar to other graph problems, wall and gates in the mantainance of a visit set

Like Combination Sum (backtracking to explore paths) 
and Walls and Gates (DFS with visited set on a grid). 
Also similar to Flood Fill for grid traversal.
 Use DFS with backtracking to try all possible paths.
Plan

"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True
        if not board or not board[0]:
            return False
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        path = set()
        directions = [[1,0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c, pos):
            if pos == len(word):
                return True
            if (not (0 <= r < ROWS) or
                not (0 <= c < COLS) or 
                (r, c) in path or 
                board[r][c] != word[pos]):
                return False

            path.add((r, c))
            if (dfs(r+1, c, pos+1) or
                dfs(r-1, c, pos+1) or
                dfs(r, c+1, pos+1) or
                dfs(r, c-1, pos+1)):
                return True
            path.remove((r, c))
            return False

            

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
        return False






