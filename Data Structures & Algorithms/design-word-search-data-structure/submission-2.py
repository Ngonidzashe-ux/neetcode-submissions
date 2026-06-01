"""
Understand:
Implement a data structure that allows the adding and searching for words efficiently
Match: Like Implement a Prefix trie, the best way is to use a trie
Plan:
init

"""

class TrieNode:
    def __init__(self):
        self.endofWord = False #pass in the character
        self.children = [None] * 26 #This is going to store the children which are also TreeNodes 

class WordDictionary:
    def __init__(self):
        self.root = TrieNode() #I am going to have a root with 0 as the starting point
        

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if not node.children[ord(char) - ord('a')]:
                node.children[ord(char) - ord('a')] = TrieNode()
            node = node.children[ord(char) - ord('a')] 
        node.endofWord = True


    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word): #If the position is >= len(word), it means you have completed the word without being stopped returning false at any point so we good.
                return node.endofWord
            char = word[i] #extract the current character we want to add
            if char == ".":
                for child in node.children:
                    if child and dfs(child, i + 1):
                        return True
                return False
            else:
                child = node.children[ord(char) - ord('a')]
                if not child:
                    return False
                return dfs(child, i+1)

        return dfs(self.root, 0)




        
