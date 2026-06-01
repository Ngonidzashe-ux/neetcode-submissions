class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)
        for r in range(len(nums) - 1, -1, -1):
            for j in range(r + 1, len(nums)):
                if nums[r] < nums[j]:
                    LIS[r] = max(LIS[r], 1 + LIS[j])
        return max(LIS)
        