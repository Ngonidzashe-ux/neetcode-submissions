# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    #Encodes a tree to a single string.
    def serialize(self, root: TreeNode) -> str:
        #set our result to an array to make things easier and then join the strings together later with a comma delimeter
        res = []
        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> TreeNode:
        #split the data into the list that we are gonna be needing
        vals = data.split(",")
        #create a pointer called self.i.
        #self because its gonna be a member of this class and its gonna be global
        #Initialise it at 0
        self.i = 0

        def dfs():
            if vals[self.i] == "N":
                #If the current index i is pointing to a null node, increment the index and return a NULL NODE
                self.i += 1
                return None
            #If not, create the node with the value
            node = TreeNode(int(vals[self.i]))
            #Increment the index
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()