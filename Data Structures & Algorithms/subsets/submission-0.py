"""
Understand:
Return all the subsets of nums
Input = List[int], output = List[List[int]]

Plan:
if not nums:
    return []
-For each number, we include or exclude in the subset
- We use a set and an index
-dfs append the subset to res and return 

NB. We dont need to pass subarray as a parameter, because we are passing it by reference and we will be referencing the orginal subset either way
So its better for us to just access it from where it is by refernce, make a copy of it.
We can use a list because popping from the end where the most recently added element is, is O(1)
If we do a decision tree, we will find out that we only need to be adding the leaf nodes 

"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        res = []
        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append((nums[i]))
            dfs(i+1)
            subset.pop()
            dfs(i+1)
 
        dfs(0)
        return res
