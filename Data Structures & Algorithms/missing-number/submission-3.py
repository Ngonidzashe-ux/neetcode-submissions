class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        loop = array = 0
        for i in range(n+1):
            loop = loop ^ i

        for n in nums:
            array = array ^ n
        return loop ^ array
        