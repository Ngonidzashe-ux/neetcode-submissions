# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def Depth(self, root, count):
#         if not root:
#             return count
#         else:
#             if root.left != None:
#                 self.Depth(root.left, count+1)
#             if root.right != None:
#                 self.Depth(root.right, count+1)

#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         count = 0
#         maxcount = 0
#         a = self.Depth(root, count)
#         if a != None and a > maxcount:
#             maxcount = a
#         return maxcount

class Solution:
    #Recursive DFS
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) 
               
