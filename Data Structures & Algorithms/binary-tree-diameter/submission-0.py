# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]
        def dfs(node):
            if not node:
                return 0
            leftMax = dfs(node.left)
            rightMax = dfs(node.right)
            curDiameter = leftMax + rightMax
            res[0] = max(res[0], curDiameter)
            return 1 + max(leftMax, rightMax)
        dfs(root)
        return res[0]

            