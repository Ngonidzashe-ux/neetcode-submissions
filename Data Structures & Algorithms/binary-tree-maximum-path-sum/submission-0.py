# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #We are making this a function because this would make it easier to modify 
        #within the recursive function
        #We are gonna initialise it with the root value
        res = [root.val]

        #return the max path sum without split
        def dfs(root):
            #base case if root is null
            if not root:
                return 0

            #Find the max from the left and right 
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            #in case they are negative, update their values first to have 0
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            #compute max path sum with split
            #root.val +leftMax + rightMax could potentially be our updated results value
            #Therefore we take a max with the current result value
            res[0] = max(res[0], root.val + leftMax + rightMax)

            #The return value is going to be what we compute without splitting
            #so we can't choose both as this would mean splitting, we need either left or right.
            return root.val + max(leftMax, rightMax)

        dfs(root)#call dfs
        return res[0]