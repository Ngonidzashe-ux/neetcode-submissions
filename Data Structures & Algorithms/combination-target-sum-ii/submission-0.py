"""
Understand:
Return a list of all combinations that sum up to the target
Input: List[int], Output = List[List[int]]
Constraints: We have duplicates in the candidates, can only use a candidate once

#have a dfs that builds a tree.
left subtree inlcueds the element, right does not 
Plan:
if not candidates:
    return []
res = []
comb = []

dfs(curSum, i)
if curSum == target:
    res.append(comb.copy())
    return
if curSum > target or i >= len(nums):
    return
comb.append(candidates[i])
curSum += candidates[i]
dfs(curSum, i+1)
comb.pop()
curSum -= candidates[i]
dfs(curSum, i+1)




"""


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        candidates.sort()
        res = []
        comb = []

        def dfs(curSum, i):
            if curSum == target:
                res.append(comb.copy())
                return
            if curSum > target or i >= len(candidates):
                return
            comb.append(candidates[i])
            curSum += candidates[i]
            dfs(curSum, i+1)
            comb.pop()
            curSum -= candidates[i]
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            dfs(curSum, i+1)
        dfs(0, 0)
        return res
