class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLength = 0
        numSet = set(nums)
        for num in numSet:
            curLength = 1
            i = num
            while (i - 1) in numSet:
                curLength += 1
                i = i - 1
            maxLength = max(maxLength, curLength)
        return maxLength