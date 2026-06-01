class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True



class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        #Create a root trienode and add all the words to the trie
        root = TrieNode()
        for w in words:
            root.addWord(w)

        #get the dimensions of the board
        ROWS, COLS = len(board), len(board[0])
        #empty sets for visited cells and the results of the dfs
        res, visit = set(), set()

#We are gonna be gong through each position in the matrix and we would want to pass in the coordinates of the position as r,c
#We want to pass on a the current trie node that we are at in our trie and what is the word so far
        def dfs(r, c, node, word):
            if (
                r not in range(ROWS) #out of bounds
                or c not in range(COLS) #out of bounds
                or board[r][c] not in node.children #If the character at the current cell is not in the trie
                or (r, c) in visit #or we have visited the cell already
            ):
                return
            #Otherwise add the cell to the visit set
            visit.add((r, c))

            #Then since we did this, we wanna update the node that we are at to be the child of the node we just visited
            node = node.children[board[r][c]]
            #update the word by adding to it the character we have just reached
            word += board[r][c]
            #check if this is the end of the word
            if node.isWord:
                node.isWord = False
                #if yes, then add to the res
                res.add(word)

#Then do dfs 4 times, basically the 4 neighbours
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            #then remove the visited cell if there is no loops and everything is okay
            visit.remove((r, c))

#We are going to do a quick nested loop inside the entire grid
        for r in range(ROWS):
            for c in range(COLS):
                #call the dfs function on each position
                dfs(r, c, root, "")

#put the res back to a list
        return list(res)
