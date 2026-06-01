class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums) #in case we have one element which happens to be negative
        curMin, curMax = 1,1

        for n in nums:
            tmp = curMax * n
            curMax = max(n * curMax, n*curMin, n)
            curMin = min(tmp, n*curMin, n)
            res = max(res, curMax)
        return res


             
