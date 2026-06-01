class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        res = []
        perm = []
        included = set()
        def dfs():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            for i in range(len(nums)):
                if i not in included:
                    perm.append(nums[i])
                    included.add(i)
                    dfs()
                    perm.pop()
                    included.remove(i)

        dfs()
        return res


            
        