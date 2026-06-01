"""
U — Understand:
Determine whether a binary tree is height-balanced. A tree is balanced if, for every node, the heights of the left and right subtrees differ by no more than 1.

M — Match:
This problem resembles other recursive tree problems like computing height or validating tree properties, which typically use post-order DFS. Each recursive call should gather information from left and right children and combine it at the current node.

P — Plan:

Use a recursive helper dfs(node) that returns a tuple: (isBalanced, height).

For each node:

Recursively get balance status and height of left and right children.

If both subtrees are balanced and the height difference is ≤ 1, mark the current node as balanced.

Return the current node’s balance status and its height (1 + max(left, right)).

Return the isBalanced part from dfs(root).
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return [True, 0]
            left = dfs(node.left)
            right = dfs(node.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])]
        
        return dfs(root)[0]
        

        