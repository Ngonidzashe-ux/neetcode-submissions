# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, root, length):
        if not root:
            return length
        return max(self.helper(root.right, 1 + length), self.helper(root.left, 1 + length))
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        length = self.helper(root, 0)
        return length
        
        