"""
Understand:
- Given a tree, encode the tree structure into a string and be able to decode the tree structure too
- Serialize: Input is a tree, output is a string
- Deserialize: Input is a string and output is a tree
-Edge cases: Tree is Null 

Match:
This could use the same tricks used in the constructing of a tree from preorder and inorder traversal.Which means serialize has to give us both these methods and then year

"""



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        
        res = []
        def preorder(node):
            if not node:
                res.append('#')
                return 
            res.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return ",".join(res)
            
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        print(data)
        preorder = data.split(",")
        self.i = 0
        print(preorder)


        def buildTree():
            if self.i >= len(preorder):
                return None
            if preorder[self.i] == "#":
                self.i += 1
                return None
            node = TreeNode(int(preorder[self.i]))
            self.i += 1
            node.left = buildTree()
            node.right = buildTree()
            return node

            

        return buildTree()
