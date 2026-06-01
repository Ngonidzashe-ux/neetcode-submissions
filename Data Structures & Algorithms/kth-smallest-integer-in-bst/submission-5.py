# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Understand:
Given the root of binary tree, return the k smallest element.
Input: Node, Output: int
Edge cases: Empty tree
Match: Like Graph Valid tree, we typically use recursion for trees to traverse through it
Plan:
if root is None:
    return 0
res = []
def inorder(root):
    if not root:
        return 
    inorder(root.left)
    res.append(root)
    inorder(root.right)

inorder(root)
return res[k - 1] if k < len(res) else 0




"""

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return 0
        res = []
        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

        inorder(root)
        return res[k - 1]