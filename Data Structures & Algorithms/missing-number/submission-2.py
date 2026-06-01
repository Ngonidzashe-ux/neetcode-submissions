class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        res = out = 0
        for i in range(n+1):
            res = res ^ i
        for num in nums:
            out = out ^ num
        return out ^ res
        