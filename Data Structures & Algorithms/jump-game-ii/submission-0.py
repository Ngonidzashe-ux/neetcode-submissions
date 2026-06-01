""""
Understand:
Return the minimum number of jumps to reach the last position in the array
Input: nums, output, int
Edge cases none
Constraints always a valid answer.

Plan:
Backtracking, for each position you have got to, go through each possible jump and backtrack if you dont get right one
minJumps = len(nums)
dfs(i, curJumps)
if i == len(nums):
    minJumps = min(minJumps, curJumps)
    return
if i > len(nums):
    return
for j in range(nums[i] + 1):
    curJumps += 1
    dfs(i+j, curJumps)
    curJumps -= 1



"""

class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l, r = 0, 0
        while r < len(nums) - 1:
            furthest = 0
            for i in range(l, r+1):
                furthest = max(i + nums[i], furthest)
            res += 1
            l = r+1
            r = furthest
        return res
        
        