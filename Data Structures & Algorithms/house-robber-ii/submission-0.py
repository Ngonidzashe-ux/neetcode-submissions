class Solution:
    def rob(self, nums: List[int]) -> int:

        def firstrob(nums):
            rob1, rob2 = 0,0
            for n in nums:
                temp1 = max(n+rob1, rob2)
                rob1 = rob2
                rob2 = temp1
            
            return rob2
        return max(nums[0], firstrob(nums[1:]), firstrob(nums[:-1]))

        