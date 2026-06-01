# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:  
    def isSametree(self, root, subroot):
        if not root and not subroot:
            return True
        if root and not subroot:
            return False
        if subroot and not root:
            return False
        if root.val != subroot.val:
            return False
        return (self.isSametree(root.right, subroot.right) 
        and self.isSametree(root.left, subroot.left))

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.isSametree(root, subRoot):
            return True
        return (self.isSubtree(root.right, subRoot) or 
                self.isSubtree(root.left, subRoot))

        