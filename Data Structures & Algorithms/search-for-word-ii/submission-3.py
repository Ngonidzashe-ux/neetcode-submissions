"""
Understand:
Given a 2d board and a list of words, return all the words that are in the list that can be found in the board.
Input: 2d list, list Output: list of the words found
Constraints:
Edge cases: Empty board, empty list


Match:
Like Word Search 1, DFS proves useful here

Plan:
The brute force approach is for each word, do backtracking starting from each cell searching for the word from the grid
The better way is to find a data structure that allows the efficient inserting and search of the words
Then for each cell, we can search if there is a prefix in the trie that starts with that and do the dfs etc
"""

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False
        self.idx = -1

    def addWord(self, word, i):
        curNode = self
        for c in word:
            index = ord(c) - ord('a')
            if not curNode.children[index]:
                curNode.children[index] = TrieNode()
            curNode = curNode.children[index]
        curNode.isEndOfWord = True
        curNode.idx = i


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not words:
            return []
        
        root = TrieNode()
        for i, word in enumerate(words):
            root.addWord(word, i)

        ROWS, COLS = len(board), len(board[0])
        res = set()
        visited = set()

        def dfs(r, c, node):
            if (r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                (r, c) in visited):
                return
            
            ch = board[r][c]
            index = ord(ch) - ord('a')
            child = node.children[index]
            if not child:
                return

            visited.add((r, c))
            if child.isEndOfWord:
                res.add(words[child.idx])
                child.isEndOfWord = False  # avoid duplicates

            dfs(r + 1, c, child)
            dfs(r - 1, c, child)
            dfs(r, c + 1, child)
            dfs(r, c - 1, child)
            visited.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root)

        return list(res)



