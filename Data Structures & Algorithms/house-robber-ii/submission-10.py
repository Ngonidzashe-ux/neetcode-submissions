class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums):
            if not nums:
                return 0
            if len(nums) == 1:
                return nums[0]
            one, two = nums[-1], 0
            for i in range(len(nums) - 2, -1, -1):
                curr = max(nums[i] + two, one)
                one, two = curr, one
            return one
        return max(helper(nums[1:]), helper(nums[:-1]), nums[0])
        