"""
Understand:
Given an array of distinct integers and a target, return the combination of integers that sum up to the target
Input: int, target, List[int], list of distinct integers, Output: List[List[int]]
Constraints: Order does not matter, no duplicates, can use any number multiple times 
Edge case, empty nums, 
Plan:
if not nums:
    return []
res = []
comb = []

make a decision tree using dfs function

dfs(i curSum, target):
if the curSum == target, then we add that combination to the res array
if the curSum > target, then we return from the function
to the current num, i:
for each of the other values including the current:
    call the function with increased curSum 



"""


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums: 
            return []
        res = []
        comb = []
        def dfs(i, curSum):
            if curSum == target:
                res.append(comb.copy())
                return
            if curSum > target or i >= len(nums):
                return
            #include the current i
            comb.append(nums[i])
            curSum += nums[i]
            dfs(i, curSum)
            curSum -= nums[i]
            comb.pop()
            dfs(i+1, curSum)

            #exclude the current i
        dfs(0, 0)
        return res