class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Hash = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in Hash:
                return [Hash[diff], i]
            else:
                Hash[nums[i]] = i
        
