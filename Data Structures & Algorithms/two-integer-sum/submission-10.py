class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        for index, num in enumerate(nums):
            diff = target - num
            x = numMap.get(diff, -1)
            if x == -1:
                numMap[num] = index
            else:
                return [numMap[diff], index]


        