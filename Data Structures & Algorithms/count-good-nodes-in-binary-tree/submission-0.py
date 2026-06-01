# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Understand:
Find all the nodes such that its value is the greatest along the path from the root to itself
Input: TreeNode, Return int, the number of the good nodes
Edge cases, root is empty

Match:

Plan:
-The root is a good node
-Then we need to count the good nodes in the left subtree and in the right
- We need to pass the greatest val that we have seen so far in the calling


"""
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxVal):
            if not node:
                return 0
            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            res+= dfs(node.left, maxVal)
            res+= dfs(node.right, maxVal)
            return res
        return dfs(root, root.val)

            
        