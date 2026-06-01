# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
1. Find a unique number that represents a node
2. Hashmap that keeps the maximum path starting at a node
3. Traverse tree from the leaves, and for each node, check if the max path is in hashmap already. If not, add it and if it is in use that and then udpate the current node value.
4. 
        
"""

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        def dfs(node):
            if not node:
                return 0
            leftMax = dfs(node.left)
            rightMax = dfs(node.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            #Compute max path with split
            res[0] = max(res[0], node.val + leftMax + rightMax)

            return node.val + max(leftMax, rightMax)
        dfs(root)
        return res[0]

      
        