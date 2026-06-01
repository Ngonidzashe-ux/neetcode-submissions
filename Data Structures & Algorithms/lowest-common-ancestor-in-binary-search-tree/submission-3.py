"""
Understand:
Return the lowest common ancestor of two nodes p and q from the a BST
Input: 3 Treenodes, One treenode
Constraints: The tree has unique values
Edge cases: root is null, one of the two nodes is null or both
Match: Like Validate Binary Tree, you have to traverse the tree recursively and check if the 
p < current node.val < q or the other way. If both p and q are greater, then go to the right, if less, go to the lest
Plan:


"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or not p or not q:
            return None
        def dfs(root):
            if not root:
                return None
            if p.val > root.val and q.val > root.val:
                return dfs(root.right)
            elif p.val < root.val and q.val < root.val:
                return dfs(root.left)
            else:
                return root
        return dfs(root)
            

       
                