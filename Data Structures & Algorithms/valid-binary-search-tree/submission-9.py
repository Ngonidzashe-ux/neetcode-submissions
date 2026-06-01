# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Understand:
Given the root of a binary tree, return true if the binary tree is valid
This means for a left child of a node, it has to be less than that node but still greater than the ancestor whose right child 
Match: Like 
Plan:
"""
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(lower, node, upper):
            if not node:
                return True
            if not (lower < node.val < upper):
                return False
            return (isValid(lower, node.left, node.val) and 
            isValid(node.val, node.right, upper))
             
        return isValid(float("-inf"), root, float("inf"))


        