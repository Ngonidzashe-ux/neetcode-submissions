# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder and not inorder:
            return None
        root = TreeNode(preorder[0], None, None)
        root_index = inorder.index(root.val)
        lefttree = self.buildTree(preorder[1: 1 + root_index], inorder[:root_index])
        righttree = self.buildTree(preorder[1 + root_index:], inorder[root_index+1:])
        root.left = lefttree
        root.right = righttree
        return root
