# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(lower, node, upper):
            if not node:
                return True
            if not (lower < node.val < upper):
                return False
            left_child = node.left
            right_child = node.right
            return valid(lower, left_child, node.val) and valid(node.val, right_child, upper)

        return valid(float("-inf"), root, float("inf"))
        
        