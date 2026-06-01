class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        def dfs(r,c,length):
            if length == len(word):
                return True
            if ((r,c) in visited or 
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                word[length] != board[r][c]
            ):
                return False
            visited.add((r,c))
            for dr, dc in directions:
                newr = r + dr
                newc = c + dc
                if dfs(newr, newc, length+1):
                    return True
            visited.remove((r,c))
            return False



        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
        return False
        