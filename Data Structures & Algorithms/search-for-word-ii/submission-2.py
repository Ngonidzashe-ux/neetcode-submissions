class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        # visited = set()
        path = set()
        res = []

        def dfs(r, c, pos, word):
            if len(word) == pos:
                return True
            if (not (0 <= r < ROWS) or
                not (0 <= c < COLS) or
                (r, c) in path      or
                # (r, c) in visited   or
                board[r][c] != word[pos]
            ):
                return False
            path.add((r, c))
            # visited.add((r, c))
            if (dfs(r + 1, c, pos + 1, word) or 
                dfs(r - 1, c, pos + 1, word) or 
                dfs(r, c - 1, pos + 1, word) or
                dfs(r, c + 1, pos + 1, word)
            ):
                return True
            path.remove((r, c))
            # visited.remove((r, c))
            return False
            

        def search(word):
            for r in range(ROWS):
                for c in range(COLS):
                    if board[r][c] == word[0]:
                        if dfs(r, c, 0, word) and word not in res:
                            res.append(word)

        for word in words:
            path = set()
            search(word)
        return res