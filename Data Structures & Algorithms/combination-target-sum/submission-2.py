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

# Make a decision tree using dfs function
#One brute force decision tree is to have a root, and decision tree nodes corresponding to each integer in the array
#Repeat that for every single node. But this does not really work as it gives us duplicate combinations
#Better way is to have 2 subtrees, one that includes a number, and another one that excludes that number and that is the one defined below

dfs():
#We start without knowing what arguments or information we want to track
#Base case:
if curSum == target:
    then add that node/array to the results
if curSum > target or i >= len(nums):
    return from the path without adding the combination to the results
#From this, we know we need to track the curSum so we have to have that in the params

Then we include the current value in the comb array, this current value is pointed to by an index so we need an i inthe params
comb.append(nums[i])
Then add it to the curSum
curSum+= nums[i]
Then we build the left branch of that tree where we still include the current index
dfs(i, curSum)
The we backtrack so we remove that coz we want to build the right tree that does not have the index i included
So remove the nums[i] and remove it from curSUm
curSum -= nums[i]
comb.pop()
then run dfs starting on the next index
dfs(i+1, curSum)
Remember dfs recursion, you are literally build a single subtree or node at a time



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