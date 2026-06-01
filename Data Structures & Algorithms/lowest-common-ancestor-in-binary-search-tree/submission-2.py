#Plan
"""
There are a few cases
1. Both greater than the root, go right
2. Both smaller than the root, go left,
3. One is greater and the other is smaller, thats the split
4. One is equal and the other greater or smaller, then that smaller is the one
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def dfs(root):
            if not root:
                return 

            if ((p.val <= root.val and q.val >= root.val) or 
                (p.val >= root.val and q.val <= root.val)
            ):
                return root
            if p.val > root.val and q.val > root.val:
                return dfs(root.right)
            if p.val < root.val and q.val < root.val:
                return dfs(root.left)

            
        return dfs(root)
            
            

