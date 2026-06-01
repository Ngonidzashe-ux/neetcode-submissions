"""
Understand:
Given an array of integers, return all the possible permutations 
Input: List[int], Output, List[List[int]]
Constraints: Permutation is same length as the original input

Plan:
if not nums:
    return []
#Recursively build a decision tree using dfs
#Have 3 choice nodes at the beginning and recursively add the missing element

res = []
perm = set()
dfs(i)
if len(perm) == len(nums):
    res.append(perm.copy)
    return
if nums[i] in perm:
    return
for j in range(len(nums)):
    perm.add(nums[j])
    dfs(j)
    perm.remove(nums[j])










"""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        for n in nums:
            new_perms = []
            for p in perms:
                for i in range(len(p) + 1):
                    p_copy = p.copy()
                    p_copy.insert(i, n)
                    new_perms.append(p_copy)
            perms = new_perms
        return perms