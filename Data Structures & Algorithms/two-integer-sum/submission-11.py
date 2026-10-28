class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffMap = {}
        for index in range(len(nums)):
            diff = target - nums[index]
            if diff in diffMap:
                return [diffMap[diff], index]
            else:
                diffMap[nums[index]] = index
            
        