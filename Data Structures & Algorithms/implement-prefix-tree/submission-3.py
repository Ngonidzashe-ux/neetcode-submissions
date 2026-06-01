"""
Understand:
Implement a prefix tree class that allows the efficient storing and retrieval of keys. Complete the methods below
Input: Different things for each function, note
Constraints: Word is made up of lowercase english characters, 
Edge cases: Word is empty or tree is empty when you do the search

Match:
Like Design a data structure to add and retrieve words efficiently, we have to use a trie

Plan:
Overview: Create our own class of a TrieNode that contains children and isEndOfWord flag. 
We dont put a character in there as the value or anything because 
the position of a node in the children array gives us back 
the character. Children array is enough.

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWorld = False

Init:
self.root = TreeNode()

Insert:
cur = self.root
for each char in word:
    index = ord(char) - ord('a')
    if not cur.children[index]:
        cur.children[index] = TrieNode()
    cur = cur.children[index]
cur.isEndOfWord = True

Search:
def dfs(node, i):
    if tracking pos i == len(word):
        return the EndOfWord flag. #Could be that the word we are looking for is actually a prefix
    #Otherwise
    char = word[i] #extract the current character
    if not node.children[ord(char) - ord('a')]:  #Check if its in the current node 
        return False
    return dfs(node.children[ord(char) - ord('a')], i+1)
                 
def dfs(node, i):
    if i >= len(word):
        return True
    char = word[i]
    if not node.children[ord(char) - ord('a')]:
        return False
    return dfs(node.children[ord(char) - ord('a')], i+1)

   


"""


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False


class PrefixTree:
    def __init__(self):
        self.root = TrieNode()


    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            index = ord(char) - ord('a')
            if not cur.children[index]:
                cur.children[index] = TrieNode()
            cur = cur.children[index]
        cur.isEndOfWord = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i >= len(word):
                return node.isEndOfWord
            char = word[i]
            if not node.children[ord(char) - ord('a')]:
                return False
            return dfs(node.children[ord(char) - ord('a')], i+1)
        return dfs(self.root, 0)
  

    def startsWith(self, prefix: str) -> bool:                  
        def dfs(node, i):
            if i >= len([prefix]):
                return True
            char = prefix[i]
            if not node.children[ord(char) - ord('a')]:
                return False
            return dfs(node.children[ord(char) - ord('a')], i+1)
        return dfs(self.root, 0)

        
        