#First thing we need to do is create our own TreeNode
#Initialise the end point marker that's gonna start with False
#Initialise a hashmap thats gonna be storing information

class PrefixTreeNode:
    def __init__(self):
        self.children = {}
        self.end = False

class PrefixTree:
    def __init__(self):
        #create the root in the initialisation method
        self.root = PrefixTreeNode()

    def insert(self, word: str) -> None:
        #Start at the root
        curr = self.root

        #Go character by character in the word
        for c in word:
            #Check if the c is in the children
            if c not in curr.children:
                #If its not, then we add it and create a new trie node
                curr.children[c] = PrefixTreeNode()
            #If the character already exists, then we are gonna move the current pointer to the character
            curr = curr.children[c]
        #After we get throught the whole word, we are gonna mark it as the end of the word
        curr.end = True


    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True
