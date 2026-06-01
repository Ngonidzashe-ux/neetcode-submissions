class TrieNode:
    def __init__(self):
        self.children = {}  # a : TrieNode
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()


    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:
        #Define a dfs function thats gonna take in the current index position 
        #where the search is starting and takes in the current node
        def dfs(j, root):
            #Initialise the current variable to the root
            cur = root
            #Go through the word starting from the index j
            for i in range(j, len(word)):
                c = word[i]
                #if the current character is dot, then:
                if c == ".":
                    #We iterate through all the the characters that are in the current level of the tree.
                    for child in cur.children.values():
                        #We call the dfs function starting from index i+1 and the child as the root
                        if dfs(i + 1, child):
                            #if this returns True, then return True
                            return True
                    #If you do not return True, then it means its false and therefore return that.
                    return False
                #If the character is not a dot, then just do the normal searching
                else:
                    #If the current character is not in the tree in the cur children, return False immediately
                    if c not in cur.children:
                        return False
                    #Otherwise, you should move the current variable to be equal to the c node that we found
                    cur = cur.children[c]
            #If we have not exited the loop, already, then we return the value of cur.word
            return cur.word

#Then call the function with the index 0 and the root of the tree.
        return dfs(0, self.root)        
