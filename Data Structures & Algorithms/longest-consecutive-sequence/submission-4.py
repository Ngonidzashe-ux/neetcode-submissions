class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numSet = set(nums)

        for num in nums:
            length = 0
            val = num
            while (val) in numSet:
                length+=1
                val += 1
            longest = max(longest, length)
        return longest

        